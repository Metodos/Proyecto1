# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:24:36 2013

@author: julio
"""

import func

def checkRange(function, a, b):
    val = False  
    if (func.evalF(function, a)*func.evalF(function, b)<0):
        val=True   
    return val

def decimalCheck(cant_deci, previo, actual):
    cero = 10**(-cant_deci)    
    
    if(abs(previo-actual)<= cero):
        return True
    else:
        return False

"""
def decimalCheck(cant_deci, previo, actual):
    checks = True
    val = False
    str_previo = str(previo)
    str_actual = str(actual)

    for i in range(len(str_previo)):
        if str_previo[i] == '.':
            previo_point = i+1
            val = True
            pass

    for i in range(len(str_actual)):
        if str_actual[i] == '.':
            actual_point = i+1
            val = True
            pass
        
    if(val):
       for i in range(cant_deci):
            if (len(str_previo) > (i+previo_point)) and (len(str_actual) > (i+actual_point)):
                if int(str_previo[i+previo_point]) != int(str_actual[i+actual_point]):
                    checks = False
                    break
            else:
                checks = False
                break 
    else:
        checks = False
    return checks
"""

def syntethicDivision(polynomio, k):
    _polynomio = []
    _polynomio.append(polynomio[0])
    
    for i in range(1,len(polynomio)):
        _polynomio.append(_polynomio[i-1]*k + polynomio[i])
        
    del _polynomio[len(_polynomio)-1]
    
    return _polynomio