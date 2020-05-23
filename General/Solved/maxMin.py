#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May 20 10:29:29 2020

@author: hankui

"""


#%% attempt 1
from itertools import combinations

def maxMin1(k, arr):
    
    diff = float("inf")
    comb = combinations(arr, k)
    
    for val in comb:
        tmp = max(val) - min(val)
        if tmp < diff:
            diff = tmp
    return diff 


#%% attempt 2
def maxMin(k, arr):
    arr1 = sorted(arr)
    ans = float('inf')
    for i in range(len(arr)-k+1):
        subgrp = arr1[i:i+k]
        diff = max(subgrp) - min(subgrp)
        
        if diff == 0:
            ans = diff
            break
        else:
            if diff < ans:
                ans = diff
    return ans 


#%% one solution
def maxMin(k, arr):
    ans = 10**9
    arr_s = sorted(arr)
    for i in range(len(arr) - k + 1):
            sub_arr_min = arr_s[i]
            sub_arr_max = arr_s[i+k-1]
            ans = min(sub_arr_max - sub_arr_min, ans)
    return ans


#%% test cases 
k = 3
arr = [1,2,1,2,1]

maxMin(k, arr)