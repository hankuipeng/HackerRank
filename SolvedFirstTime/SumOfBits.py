#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:57:59 2019

@author: hankui
"""

# https://practice.geeksforgeeks.org/problems/find-sum-of-different-corresponding-bits-for-all-pairs/0

#%%
arr = [1, 3, 5] 
n = len(arr) 


#%% sum of bit differences among all pairs
# source: 

def sumBitDifferences(arr, n): 
  
    ans = 0  # Initialize result 
  
    # traverse over all bits 
    for i in range(0, 32): 
      
        # count number of elements with i'th bit set 
        count = 0
        for j in range(0,n): 
            if ( (arr[j] & (1 << i)) ): 
                count += 1
  
        # Add "count * (n - count) * 2" to the answer 
        ans += (count * (n - count) * 2); 
      
    return ans 


#%%
from itertools import permutations
import numpy as np
def BitDiff(arr): 
    
    # initialised answer
    count = 0
    
    # the length of the array
    n = len(arr)
    
    # obtain the binary representation for every number in the array
    br = [] # initialise an empty list 
    for i in range(0,n):
        br_i = str(bin(arr[i]))[2:]
        br.append(br_i)
    
    # get all combinations of length 2
    comb = list(permutations(list(range(0,n)), 2))
    
    for ii in comb:
        
        str_a = br[ii[0]];
        str_b = br[ii[1]];
        # maximum length of the two strings being compared
        max_len = max(len(str_a), len(str_b))
        
        # minimum length of the two strings being compared 
        min_len = min(len(str_a), len(str_b))
        
        # append zeros to the end of the shorter string
        ind = np.argmin([len(str_a), len(str_b)])
        str_short = br[ii[ind]]
        str_short = str_short.ljust(max_len, '0')
        
        for l in range(max_len):
            if str_short[l] != br[ii[1-ind]][l]:
                count += 1
        
    
    return count


#%% one correct submission
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans = 0  # Initialize result 
  
    # traverse over all bits 
    for i in range(0, 32): 
      
        # count number of elements with i'th bit set 
        count = 0
        for j in range(0,n): 
            if ( (arr[j] & (1 << i)) ): 
                count+=1
  
        # Add "count * (n - count) * 2" to the answer 
        ans =(ans+ (count * (n - count) * 2))%(pow(10,9)+7); 
    print(ans)


#%%
t=int(input())
res = BitDiff(arr)
    
#%%
print(sumBitDifferences(arr, n))    
