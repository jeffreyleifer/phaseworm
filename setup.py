# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""
from setuptools import setup

import inspect
import os
import sys
import pkg_resources

# Check if TensorFlow is installed and if the version is >= 2.0
try:
    tensorflow_version = pkg_resources.get_distribution("tensorflow").version
    if pkg_resources.parse_version(tensorflow_version) < pkg_resources.parse_version("2.0"):
        raise Exception("TensorFlow version must be >= 2.0")
except pkg_resources.DistributionNotFound:
    raise Exception("TensorFlow is not installed")


# Import the version string.
path = os.path.join(os.path.abspath(os.path.dirname(inspect.getfile(
    inspect.currentframe()))), 'phaseworm_sources')
sys.path.insert(0, path)
from __init__ import __version__

with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

setup(
    name='phaseworm',
    packages=['phaseworm_sources', 'phasenet'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['phaseworm = phaseworm_sources.phaseworm:main',
                            'stationxml2hinv = phaseworm_sources.stationxml2hinv:main'],
        },
    version=__version__,
    description='A Python wrap-up of PhaseNet for use with EarthWorm',
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author='Jean-Marie Saurel',
    author_email='saurel@ipgp.fr',
    url='http://www.ipgp.fr',
    license='GNU Lesser General Public License, Version 3 (LGPLv3)',
    platforms='OS Independent',
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Physics'],
    python_requires='>=3.6,<3.9',
    )
