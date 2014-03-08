#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

import subprocess, os, sys

def install():
    R_install_dir = '%s/R' % (os.environ['HOME'],)
    try:
        os.mkdir(R_install_dir)
    except OSError:
        pass
    ccmd = 'R CMD INSTALL -l %s .' % (R_install_dir,)
    subprocess.call(ccmd.split(' '))

if sys.argv[1] not in ('egg_info',):
    install()

setup(
    name='xcms',
    version='1.93.2',
    description='Update to 1.93.2 version of xcms',
    author='Benjie Chen',
    author_email='benjie@alum.mit.edu',
    long_description=open('README.md', 'r').read(),
    packages=[],
    zip_safe=False,
    requires=[],
    install_requires=[],
    classifiers=[
      'Operating System :: OS Independent',
      'Programming Language :: R',
      'Topic :: Utilities'
    ],
)

