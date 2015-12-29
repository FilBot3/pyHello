pyHello
-------

A simple Python Module that displays "Hello World" using Python Modules, Executables, and in IDLE. 

To get this module, clone it from GitHub

To install this module: 

  $> python setup.py install


or to do a development "install"  


  $> python setup.py develop

The module can then be accessed through IDLE  

  >>> from pyHello.pyHello import main
  >>> print( main() )

If the $PYTHON_HOME/Scripts directory is in your $PATH, then you  have access to the command line application  

  $> pyHello ARG

The module can also be accessed via Python itself.  

  $> python -m pyHello ARG

Sources:

1. https://python-packaging.readthedocs.org/en/latest/index.html
2. https://gehrcke.de/2014/02/distributing-a-python-command-line-application/


