#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:14:59 2020

@author: hankui
"""


#%%
def largestPermutation(k, arr):
    ans = arr.copy()
    arr_des = sorted(arr, reverse = True)
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    if k >= 1:
        for i in range(k):
            if arr[i] == arr_des[i]:
                pass
            else:
                idx = [ind for ind,val in enumerate(arr) if val==arr_des[i]][0]
                swap = arr[i]
                arr[i] = arr_des[i]
                arr[idx] = swap
        ans = arr
    return ans


#%%
k = 2
arr = [4,2,3,5,1]


#%%
largestPermutation(k, arr)


#%% solution
# reference: https://www.geeksforgeeks.org/largest-permutation-k-swaps/
def largestPermutation(k, arr): 
    
    n = len(arr)

    # Auxiliary array of storing the position of elements 
    pos = {} 
    for i in range(n): 
        pos[arr[i]] = i 
  
    for i in range(n): 
  
        # If K is exhausted then break the loop 
        if k == 0: 
            break
  
        # If element is already largest then no need to swap 
        if (arr[i] == n-i): 
            continue
  
        # Find position of i'th largest value, n-i 
        temp = pos[n-i] 
  
        # Swap the elements position 
        pos[arr[i]] = pos[n-i] 
        pos[n-i] = i 
  
        # Swap the ith largest value with the value at  
        # ith place 
        arr[temp], arr[i] = arr[i], arr[temp] 
  
        # Decrement K after swap 
        k = k-1
    return arr



