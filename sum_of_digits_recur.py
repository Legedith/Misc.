# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:16:52 2018

@author: DSC
"""

def sod(x):
    """
    Input - an integer
    Output - Sum of digits
    """
    if x==0:
        return 0
    return (x%10) + sod(x//10)
print(sod(345))