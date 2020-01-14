#== Why Use Modules? ==

# Keep Python files small
# Reuse code across multiple files by importing
# A module is just a Python file!

#== Built-in Modules? ==

# Google "Python Module Index" 
# import anytime 

#== External Modules? ==

# Download from pypi.python.org
# install pip in terminal using:
# python -m pip install NAME_OF_PACKAGE
# ( help(NAME_OF_PACKAGE) )

#== Formula ==

# 1. 
# import module_name 

# module_name.method_name()

import random as omg_so_random

omg_so_random.choice(["apple", "banana", "cherry", "durian"])
omg_so_random.shuffle(["apple", "banana", "cherry", "durian"])

# 2. Importing Parts of a Module
# from MODULE_name import method_name1, method_name2


#== Custom Modules ==

# import module_name 

# module_name.method_name()

# (module_name can be the python file name) 
# (method_name can be the function name in that file)



#== Exerciese ==

# 1. Math
import math
 
answer = math.sqrt(15129)