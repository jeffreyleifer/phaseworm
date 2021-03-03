# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""
from setuptools import setup

import inspect
import os
import sys

# Import the version string.
path = os.path.join(os.path.abspath(os.path.dirname(inspect.getfile(
    inspect.currentframe()))), 'phaseworm')
sys.path.insert(0, path)
from __init__ import __version__


setup(
    name='phaseworm',
    packages=['phaseworm', 'phaseworm.phasenet'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['phaseworm = phaseworm.phaseworm:main'],
        },
    version=__version__,
    description='A Python wrap-up of PhaseNet for use with EarthWorm',
    long_description='A Python wrap-up of PhaseNet for use with EarthWorm',
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
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Physics'],
    install_requires=['obspy>=1.2', 'tensorflow>=2.0']
    )
