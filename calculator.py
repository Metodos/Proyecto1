# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:21:20 2013

@author: julio
"""

import methods_lib

print "\nBiseccion"
print methods_lib.biseccion("f2",1,10,5)

print "\nFalsa Posicion"
print methods_lib.falsaposicion("f2",1,10,5)

print "\nRecorrida"
print methods_lib.recorrida("f2",1,10,5)

print "\nNewton Raphson"
print methods_lib.newtonRaphson("f0", "f1", 0, 5)