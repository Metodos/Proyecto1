# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:46:06 2013

@author: Diego
"""

import math

print "="

def f(x):
    print x
    return math.log(x)-math.sin(x)

def recorrida(function,a,b,decimales):
    tolerancia=1.0/(10.0**decimales)  
    print tolerancia
    low=a
    up=b
    intervalo=abs((up-low)/10)
    print intervalo
    print "*"
    while (intervalo>tolerancia):
        intervalo=abs((up-low)/10)
        xo=low
        print xo
        xf=low+intervalo
        print xf
        while(xo<up):
            if (((eval(function+"("+str(xf)+")"))*(eval(function+"("+str(xo)+")")))<0):
                low=xo
                up=xf
                intervalo=(up-low)/10
                print (intervalo>tolerancia)
                print intervalo
                break
            xo=xf
            xf=xf+intervalo
    return (low+up)/2
    
    
    
A=1.0
B=10.0
root=recorrida("f",A,B,5.0)
print "Raiz= ",round(root,5)
    
    
        
            