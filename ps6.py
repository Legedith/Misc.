# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:00:46 2018

@author: DSC
"""
balance = float(input("balance: "))
annualInterestRate = float(input("annualInterestRate: "))
monthlyInt = annualInterestRate/12
low = balance /12
high = (balance*(1+monthlyInt)**12)/12
guess = (low+high)/2
steps=0
temp = balance
while abs(balance)>0.01:
    balance = temp
    steps+=1
    guess = (low+high)/2
    for i in range(12):
        unpaid_balance = balance - guess
        interest = unpaid_balance * annualInterestRate/12.0
        balance = unpaid_balance + interest
        print(balance,guess)
    if balance <0:
        high = guess
    elif balance >0:
        low = guess
print("Lowest Payment: ",round(guess,2))

