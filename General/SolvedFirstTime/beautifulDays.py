#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May  6 14:40:48 2020

@author: hankui

"""


#%%
def beautifulDays(i, j, k):
    ans = 0
    for num in range(i,j+1):
        inp = str(num)
        out = int(inp[::-1])
        if (num-out)%k == 0:
            ans += 1
    return ans 


#%%
i = 20
j = 23
k = 6


#%%
beautifulDays(i,j,k)