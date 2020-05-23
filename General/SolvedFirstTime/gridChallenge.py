#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:35:58 2020

@author: hankui
"""


#%%
grid = ['e','b','a','c','d','f','g','h','i','j','o','l','m','k','n',
        't','r','p','q','s','x','y','w','u','v']


#%%
grid=['kc', 'iu']


#%%
def gridChallenge(grid):
    
    ans = 'YES'
    n = len(grid)
    arr = []
    for i in range(n):
        arr.append(list(grid[i]))
    [arr[i].sort() for i in range(len(arr))]
    for j in range(len(arr[0])):
        col = [arr[ind][j] for ind in range(len(arr))]
        if sorted(col) != col:
            ans = 'NO'
            break
    return ans