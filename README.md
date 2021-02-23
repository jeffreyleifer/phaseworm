# PhaseWorm

This python script wraps-up PhaseNet (ref) for use as a picker within
an EarthWorm installation.

PhaseWorm can access data from 3 differents data sources, using ObsPy clients :
* SeedLink
* FDSN webservice
* EarthWorm WaveServerV

Picks can be written as EarthWorm **TYPE_PICK_SCNL** messages files or simply
written to the standard output.

PhaseWorm can run in an infinite loop in an almost real-time manner
and can also process (replay) old data.

**PhaseNet** identifies P and S arrivals and **PhaseWorm** binds them to,
respectively, vertical and horizontal channels.

---
## Installation and configuration
#### Dependencies
The _PhaseWorm_ code has been tested with **Python 3** and **ObsPy 1.2.2** and
**EarthWorm v7.10**.
The _PhaseNet_ included version uses **TensorFlow 2**.

We recommend to use an `anaconda` environment.
Instructions are given in the `phasenet/README` file.

git clone

#### EarthWorm
_PhaseWorm_ is designed to output **TYPE_PICK_SCNL** EarthWorm messages files
that will be read by the _file2ew_ module and injected into a RingBuffer.

Because _PhaseNet_ is designed to use overlapping time sequences,
it is recommended to use a _pkfilter_ module to remove duplicated picks.

_Binder_ew_ module should be setup as usual, according to the local area
settings. However, to take full advantage of the **P** and **S** phase
identifications from _PhaseNet_, two parameters should be activated :
* `no_S_on_Z` (only _PhaseNet_ **P** readings are sent on vertical channels)
* `no_P_on_Horiz` (only _PhaseNet_ **S** readings are sent on horizontal channels)

Because _PhaseNet_ picks **S** readings, it's important to set `ReportS` key
to `1` in _eqassemble_ module.

---
## Usage
By default, PhaseWorm will use the configuration from the **config.cfg** file.
```sh
phaseworm
```
Alternative configuration file can be passed on the command line.
```sh
phaseworm --config-file /my/path/to/my_config.cfg
```
The configuration file is divided into 3 different sections.

#### EarthWorm section
This section defines variables linked to the EarthWorm setup that will be used
to process the pick messages (`module_id`, `inst_id`, `message_id`).
This section also defines the directory in which **TYPE_PICK_SCNL** messages
will be written to.

#### PhaseNet section
This section defines PhaseNet related variables.
Currently there is only one available variable : the neural network training
file to use.
The recommended default is to use the file shipped with PhaseNet and
included in this bundle.

If you have trained PhaseNet on your own data, you might want to use
your training file.

#### General section
The general section contains various variables to set-up _PhaseWorm_ :
* data source
* time window lenght to process
* network.stations to look for
* channels priority list to look for each station
* **replay** or **real-time** mode
* whether to activate or not the **TYPE_PICK_SCNL** message writing.

---
## Examples
Two configuration examples are shipped : _config_replay.cfg_ and _config_rt.cfg_.

#### Replay mode
The file _config_replay.cfg_ contains a configuration for replay use.

PhaseWorm reads data from FDSN webservice, starting from xxx until xxx.

#### Real-time mode
The file _config_rt.cfg_ contains a configuration for near real-time use.

PhaseWorm reads data from an EarthWorm WaveServerV (recommended) or SeedLink.

PhaseWorm write picks in the **TYPE_PICK_SCNL** directory.

---
## Acknowledgements
_PhaseNet_ code was simplified on purpose by Weiqiang Zhu.

Data preprocessing was designed and implemented by Lise Retailleau.

Overall wrapping was done by Jean-Marie Saurel.

Claudio Satriano provided extensive code review.

Testing was performed on Mayotte seismo-volcano crisis for the
Réseau de surveillance volcanologique et sismologique de Mayotte : [REVOSIMA](
http://www.ipgp.fr/revosima).
