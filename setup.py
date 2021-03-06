#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='Facial Recognition',
      version='0.1',
      description='SE 321 Project 1',
      author='Algorithim Architects',
      packages=find_packages(),
      entry_points={'console_scripts': ['facerec=facial_recognition.cli.facerec:facerec']},
      package_data={'facial_recognition': ['includes/*']},
      )
