#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
#

"""
The main script that prints Hello World.
"""

import sys

"""
The main() that will be imported to print Hello World.
It will also print the first CLI argument. 
"""
def main() :
  print("Hello world from Python!\n")
  print( sys.argv[1:] )
# End def main()

