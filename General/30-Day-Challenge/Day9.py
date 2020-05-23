#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:19:55 2019

@author: hankui
"""

#%%
n = 3


#%%
def factorial(n):
    ans = 1
    if n <= 1:
        print(ans)
    else:
        i = 0
        while i < n:
            ans = ans*(n-i)
            i += 1
        print(ans)