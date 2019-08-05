# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 00:44:48 2018

@author: DSC
"""

s = 'azcbobobegghakl'
k=0
j=1
n=''
temp=''
for i in s:
  if s[j-1] >= i:
       n+=i
       print(n,i)
  elif len(temp)<len(n):
      temp=n
      n=''
      print('*'+temp)
  j+=1
print (i+str(j))