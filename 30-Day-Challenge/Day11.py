#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:47:38 2019

@author: hankui
"""

#%%
arr = [[1, 1, 1, 0, 0, 0,],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]


#%%
arr = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]


#%%
#CurMax = 0 # current maximum sum
CurMax = int()
for j in range(len(arr[0])-2): # loop through each column
    for i in range(len(arr)-2): # loop through each row 
        TmpSum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        if i == 0 and j == 0:
            CurMax = TmpSum
        if TmpSum > CurMax:
            CurMax = TmpSum
        