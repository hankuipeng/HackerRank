#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:59:25 2020

@author: hankui
"""


#%% attempt 1
def superDigit0(n, k):
    
    inp = str(n)*k
    curSum = sumDigits(inp)
    curDig = str(curSum)
    
    while len(curDig) > 1:
        curSum = sumDigits(curDig)
        curDig = str(curSum)
    return int(curDig) 

def sumDigits(inp):
    curSum = 0 # current sum
    for i,v in enumerate(inp):
        curSum += int(v)
    return curSum


#%% solution 1
def superDigit(n, k):
    
    def add_digits(string):
        if len(string) == 1:
            return int(string)
        result = sum(int(s) for s in string)
        return add_digits(str(result))
    
    #import pdb
    #pdb.set_trace()
    start = sum([int(s) for s in str(n)]) * k
    
    return add_digits(str(start))


#%%
n = 123
k = 3

superDigit(123,3)

