# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:24:08 2013

@author: julio
"""

import math

#   f(x)
def f0(x):
    return (math.e**(-x)-x)

#   f'(x)
def f1(x):
    return (-math.e**(-x)-1)

#   f''(x)
def f2(x):
    return math.log(x) - math.sin(x)
    
#   f'''(x)
def f3(x):
    return 0
    
def evalF(name, x):
    return eval(name+"("+str(x)+")")