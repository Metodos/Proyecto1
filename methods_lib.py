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
        print 'La raiz de f(x) es: ',m
        val=False
    else:
        val=True
        
    i=1
    while val:
        
        print 'Iteracion ',i,': ',m, 'f(m): ', func.evalF(function, m)
        
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
    
    print 'La aproximacion a la raiz es: ',m, 'f(m): ', func.evalF(function, m) 
    
    return m
    
def falsaposicion(function, a, b, decimal):
    
    xl = a
    xu = b
   
    val=True

    xr = _fpformula(function, xl, xu)
    
    i = 1    
    
    print 'Iteracion ',i,': ',xr
        
    if utilities.checkRange(function, xl, xr):
        xu = xr
    else:
        xl = xr
        
    while val:    
        
        prev_xr = xr
        xr = _fpformula(function, xl, xu)
            
        print 'Iteracion ',i,': ',xr
        
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
    tolerancia=1/(10^decimal)    
    low=float(a)
    up=float(b)
    intervalo=(up-low)/10
    while (intervalo>tolerancia):
        xo=low
        xf=low+intervalo
        while(xo<up):
            xo=xf
            xf=xf+intervalo
            if(utilities.checkRange(function,xf,xo)):
                low=xo
                up=xf
                intervalo=(up-low)/10
                break
    return (low+up)/2

def newtonRaphson(function, funcPrime, x, decimal):
        
    val = True
    
    while(val):
        prev_x = x
        x = x - (func.evalF(function, x)/func.evalF(funcPrime, x))
        
        print prev_x
        print x        
        
        if(utilities.decimalCheck(decimal, prev_x, x)):
            val = False
    
    return x
        
