# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:29:17 2018

@author: DSC
"""

def ser(x):
    '''
    sum of n natural numbers upto n
    '''
    if x<=0:
        return 0
    return x+ ser(x-1)
print(ser(5))