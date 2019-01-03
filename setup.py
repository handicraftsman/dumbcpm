#!/usr/bin/env python

from setuptools import setup

setup(name='dumbcpm',
      version='0.1.0',
      description='Possibly very dumb package manager for C/++, written in Python.',
      author='Nickolay Ilyushin',
      author_email='nickolay02@inbox.ru',
      url='https://github.com/handicraftsman/dumbcpm/',
      license='MIT',
      packages=['dumbcpm'],
      classifiers=[
          'Programming Language :: C',
          'Programming Language :: C++',
          'Topic :: Software Development :: Build Tools',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux'
      ])
