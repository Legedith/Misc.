# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:31:47 2018

@author: DSC
"""

from math import *
#saved me from writting math.tan & math.pi everytime
def polysum(n,s):
    """
    Input -> Number of sides(n) & Length of each side(s)
    output -> sum of area and square of perimeter
    """
    return round(((0.25*n*s*s)/(tan(pi/n))+(n*s)**2),4)
#used the formula given