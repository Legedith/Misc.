# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:11:01 2018

@author: DSC
"""

balance = float(input("balance: "))
annualInterestRate = float(input("annualInterestRate: "))
monthlyPaymentRate = float(input("monthlyPaymentRate "))
for i in range(12):
    minimum_payment= balance*monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    interest = unpaid_balance * annualInterestRate/12.0
    balance = unpaid_balance + interest
print("Remaining balance: ",round(balance,2))
