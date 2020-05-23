#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 16 13:43:02 2020

@author: hankui

"""


#%%
def minimumAbsoluteDifference(arr):
    
    arr_st = sorted(arr)
    n = len(arr)
    diff = []
    for i in range(n-1):
        diff.append(arr_st[i+1]-arr_st[i])
    
    return min(diff)


#%%
arr = [1, -3, 71, 68, 17]
minimumAbsoluteDifference(arr)
