#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

from setuptools import setup

"""
This file is used for installing this Python Package/Module to the local system,
or uploading it to the PyPI reposiotry and many other functions. 
Readup on easy_setup and setuptools 
"""

"""
readme() opens the README.rst to be displayed in the long_description
"""
def readme() :
  with open('README.rst') as f :
    return f.read()
  # end OPEN
# End of def readme() 

setup(
  name='pyHello',
  version='0.1.0',
  description="Simply prints Hello World.",
  long_description=readme(),
  url="http://github.com/predatorian3/pyHello",
  author="Phillip Dudley",
  author_email='Predatorian3@gmail.com',
  license='MIT',
  packages=['pyHello'],
  test_suite='nose.collector',
  tests_require=['nose'],
  include_package_data=True,
  zip_safe=False,
  scripts=['bin/pyHello']
)

