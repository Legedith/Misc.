# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 00:23:39 2018

@author: DSC
"""
s='qwertyuiopasdfghjklzxcvbnm'
i=0
j=1
n=0
a=''
while j<len(s)-1:
    n=0
    while s[j]>=s[i]:
        if j<len(s)-1:
            n+=1
            j+=1
            i+=1
        else:
            j+=1
            break
    if len(a) < len(s[i-n:j]): a = s[i-n:j]
    i+=1
    j+=1
print('Longest substring in alphabetical order is: '+a)