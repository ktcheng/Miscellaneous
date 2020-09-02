# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:49:51 2020
@author: Kellen Cheng
"""

# Relevant Import Statements
import numpy as np

### Manual Exponential Linear Regression

def quad_regression(X, Y):
    params = np.array((np.polyfit(X, Y, 2)))
    
    a = params[0]
    b = params[1]
    c = params[2]
    
    result = []
    
    for x in X:
        f = a * (x ** 2) + b * x + c
        result.append(f)
        pass
    
    return(result)
