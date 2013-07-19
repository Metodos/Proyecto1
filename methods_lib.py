# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:29:30 2013

@author: julio
"""

import utilities
import func

def biseccion(function, a, b, decimal):

    m=(a+b)/2.0

    if (func.evalF(function, m)==0):
        val=False
    else:
        val=True
        
    i=1
    while val:
        
        if utilities.checkRange(function, a, m):
            b=m
        else:
            a=m
            
        prev_m = m
        m=(a+b)/2.0
        if utilities.decimalCheck(decimal, prev_m, m):
        #if abs(f(polynomio, m))<cero and utilities.decimalCheck(decimal, prev_m, m):
            val=False
            
        i=i+1    
    return m
    
def falsaposicion(function, a, b, decimal):
    
    xl = a
    xu = b
   
    val=True

    xr = _fpformula(function, xl, xu)
    
    i = 1    
            
    if utilities.checkRange(function, xl, xr):
        xu = xr
    else:
        xl = xr
        
    while val:    
        
        prev_xr = xr
        xr = _fpformula(function, xl, xu)
        
        if utilities.checkRange(function, xl, xr):
            xu = xr
        else:
            xl = xr
            
        if(utilities.decimalCheck(5, prev_xr, xr)):
            val = False
        i = i+1
        
    return xr

def _fpformula(function, xl, xu):
    return ((func.evalF(function, xu)*(xl-xu))/(func.evalF(function, xu)-func.evalF(function, xl))) + xu
    
    
def recorrida(function,a,b,decimal):
    tolerancia=1.0/(10.0**decimal)  
    low=float(a)
    up=float(b)
    intervalo=abs((up-low)/10)
    while (intervalo>tolerancia):
        intervalo=abs((up-low)/10)
        xo=low
        xf=low+intervalo
        while(xo<up):
            if(utilities.checkRange(function, xf, xo)):
                low=xo
                up=xf
                intervalo=(up-low)/10
                break
            xo=xf
            xf=xf+intervalo
    return (low+up)/2

def newtonRaphson(function, funcPrime, x, decimal):
        
    val = True
    
    """
    i = 0
    diverging = False
    """
    
    while(val):
        prev_x = x
        x = x - (func.evalF(function, x)/func.evalF(funcPrime, x))      
        
        """        
        if(x-prev_x < 0):
            if(diverging):
                i = i+1
            else:
                i=0
                diverging=True
        """
    
        if(utilities.decimalCheck(decimal, prev_x, x)):
            val = False
    
    return x