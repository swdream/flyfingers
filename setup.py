#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import flyfingers

requisites = []

setup(
    name='flyfingers',
    version=flyfingers.__version__,
    description='Learn to type 10 fingers',
    scripts=['scripts/flyfingers'],
    long_description=open('README.rst').read(),
    author='Thanh Nguyen Tuong',
    author_email='ngtthanh1010@gmail.com',
    packages=['flyfingers'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
