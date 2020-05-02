#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Apr 29 14:18:28 2020

@author: hankui

"""


#%%
from collections import defaultdict
def pairs(k, arr):
    pos = defaultdict(list)
    n = len(arr)
    prs = []
    
    for i in range(n):
        pos[arr[i]] = i
    
    for i in range(n):
        if type(pos[arr[i]+k]) == int:
            ind = pos[arr[i]+k] # index of the value 'arr[i]+2' in the original array 
            prs.append([arr[i], arr[ind]])
        if type(pos[arr[i]-k]) == int:
            ind = pos[arr[i]-k]
            prs.append([arr[i], arr[ind]])
        
    return int(len(prs)/2) 


#%%
k = 2
arr = [1,5,3,4,2]


#%%
pairs(k, arr)