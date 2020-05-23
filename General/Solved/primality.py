#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat May  2 11:23:47 2020

@author: hankui

"""


#%% attempt 1
def primality1(n):
    d = 2
    ans = 'Prime'
    if n == 1:
        ans = 'Not prime'
    while d < n:
        if n%d == 0:
            ans = 'Not prime'
        d += 1
    return ans 


#%% attempt 2
# only need to check up to square root of n
# also no need to check for even numbers

from math import sqrt

def primality(n):
    d = 2
    ans = 'Prime'
    if n == 1:
        ans = 'Not prime'
    while d < int(sqrt(n)+1):
        if n%d == 0:
            ans = 'Not prime'
        d += 1
    return ans 