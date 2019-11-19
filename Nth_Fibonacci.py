#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:45:44 2019

@author: hankui
"""

n = 5

# https://practice.geeksforgeeks.org/problems/nth-fibonacci-number/0
#%% get the n-th Fibonacci number 
for _ in range(int(input())):
    ord=int(input())
    #arr=int(input())
    fib = [1,1]
    for i in range(2,ord):
        fib.append(fib[i-1] + fib[i-2])

    
    print(fib[ord-1]%1000000007)
