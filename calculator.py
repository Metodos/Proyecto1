# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:21:20 2013

@author: julio
"""

import methods_lib

print "\nCalculadora:"

print "\nBiseccion -> f2(x)"
print methods_lib.biseccion("f2",1,10,5)

print "\nFalsa Posicion -> f2(x)"
print methods_lib.falsaposicion("f2",1,10,5)

print "\nRecorrida -> f2(x)"
print methods_lib.recorrida("f2",1,10,5)

print "\nNewton Raphson -> f0(x)"
print methods_lib.newtonRaphson("f0", "f1", 0, 5)

print "\nSecant Method -> f0(x)"
print methods_lib.secant("f0", 1, 5, 5)