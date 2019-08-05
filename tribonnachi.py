# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 23:54:25 2018

@author: DSC
"""

def tribonacci(signature, n):
    """Gives n elements of tribonacchi give the signature i.e. first 3 elements
        and number of elements"""
    if n >3:
        for i in range(3,n):
            signature.append(signature[i-1]+signature[i-2]+signature[i-3])
    return signature[:n]
l = tribonacci([1,1,1], 8)