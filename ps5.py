# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:11:01 2018

@author: DSC
"""

balance = float(input("balance: "))
annualInterestRate = float(input("annualInterestRate: "))
high = balance
minPay= 0
while True:
    minPay+=10
    balance = high        
    for i in range(12):
        unpaid_balance = balance - minPay
        interest = unpaid_balance * annualInterestRate/12.0
        balance = unpaid_balance + interest
    if balance <=0:
        break;
print("Lowest Payment: ",round(minPay,2))
