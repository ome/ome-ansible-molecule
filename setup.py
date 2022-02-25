#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dependencies for testing OME Ansible roles
"""

# Based on
# https://github.com/pypa/sampleproject/blob/a9c1287d5f9825d8d8fce32f7ab4bc7813b97179/setup.py

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ome-ansible-molecule',
    version='0.6.0',

    description='Dependencies for testing OME Ansible roles',
    long_description=long_description,

    url='https://github.com/ome/ome-ansible-molecule',

    author='The Open Microscopy Team',
    author_email='ome-devel@lists.openmicroscopy.org.uk',

    # Choose your license
    license='GPLv2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: BSD License",

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='ansible molecule testing',

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'ansible==2.9.27',
        'docker-compose==1.26.2',
        'molecule==2.22',
        'jmespath==0.10.0',
        'passlib==1.7.4; sys_platform=="darwin"',
        # https://github.com/ansible-community/ansible-lint/issues/1795
        "rich<11.0.0",
    ],
    python_requires='>=3.6',
)
