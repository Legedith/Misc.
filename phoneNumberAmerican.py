# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 01:08:06 2018

@author: DSC
"""

n=[9,8,1,5,6,1,7,4,4,2]
a=''
for i in n[0:3]:
    a+=str(i)
b=''
for i in n[3:6]:
    b+=str(i)

c=''
for i in n[6:]:
    c+=str(i)
s='('+str(a)+") "+str(b)+"-"+str(c)
#"({}{}{}) {}{}{}-{}{}{}{}".format(*n) is better solution