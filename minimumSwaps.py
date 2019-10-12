#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:20:26 2019

@author: hankui
"""

#%%
arr = [4,3,1,2]


#%%
def minimumSwaps(arr):
    
    swaps = 0
    arr = [(x - 1) for x in arr]
    n = len(arr)
    #import pdb; pdb.set_trace()
    for ind, val in enumerate(arr[:-1]):
        if arr[ind] != ind:
            vall = arr[ind] # value of the left point to be swapped 
            
            # find the smallest value to its right 
            val_small = min(arr[(ind+1):])
            
            
            indr = arr.index(val_small) # index of the right point to be swapped
    
            ## do the swapping
            copy = vall
            arr[ind] = arr[indr]
            arr[indr] = copy
            
            swaps = swaps + 1 
    if arr[n-1] != (n-1):
        swaps = swaps + 1
    return swaps

#%%
minimumSwaps(arr)