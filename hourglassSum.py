#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:35:36 2019

@author: hankui
"""

arr = [[1,2,3], [4, 5, 6], [7,8,9]]


#%%
arr=[[-1, -1, 0, -9, -2, -2],
      [-2, -1, -6, -8, -2, -5],
      [-1 ,-1, -1, -2 ,-3, -4],
      [-1, -9, -2, -4, -4, -5],
      [-7, -3, -3 ,-2, -9, -9],
      [-1, -3, -1 ,-2 ,-4, -5]]
#%%
def hourglassSum(arr):
    n = len(arr[0])
    i = 1
    j = 1
    CurrSum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
    
    #CurrSum = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            tmp = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if tmp > CurrSum:
                CurrSum = tmp
    print(i)
    return CurrSum