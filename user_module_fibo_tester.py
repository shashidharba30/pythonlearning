import fibo_module_example as fibo
#from fibo_module_example import fib, fib2
# from fibo_module_example import *



#A module is a file containing Python definitions and statements
#the module’s name (as a string) is available as the value of the global variable __name__
#module search path
# The directory containing the input script (or the current directory when no file is specified)
# PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH)
# The installation-dependent default (by convention including a site-packages directory, handled by the site module)

fib = fibo.fib
fib(500)



#Refrence
# https://docs.python.org/3/tutorial/modules.html

#dir() is used to find out which names a module defines
import builtins
print(dir(builtins))

## collection of modules is called as a package
#The __init__.py files are required to make Python treat directories containing the file as packages
# When importing the package, Python searches through the directories on sys.path looking for the package subdirectory
#package structure
"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""
