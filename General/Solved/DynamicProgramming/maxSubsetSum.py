#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May  3 15:58:46 2020

@author: hankui

"""


#%% attempt 1
from collections import defaultdict
def maxSubsetSum1(arr):
    
    arr1 = sorted(arr, reverse=True)
    li = defaultdict(list)
    for i in range(len(arr)):
        li[arr[i]] = i
    
    ans_li = [arr1[0]]
    
    for i in range(1, len(arr)):
        #import pdb
        #pdb.set_trace()
        diff = [abs(li[arr1[i]] - li[v]) <= 1 for v in ans_li]
        if sum(diff) == 0 and arr1[i] > 0:
            ans_li.append(arr1[i])
    
    
    return sum(ans_li) 


#%% attempt 2
from collections import defaultdict
arr1 = sorted(arr, reverse=True)
li = defaultdict(list)
for i in range(len(arr)):
    li[arr[i]] = i

ans_li = arr1[0]

for i in range(1, len(arr)):
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    if abs(li[arr1[i]] - li[ans_li[-1]]) > 1 and arr1[i] > 0:
        ans_li.append(arr1[i])


#%% attempt 3 (2020/05/07)
def maxSubsetSum(arr):
    CurMax = [0]
    
    # iterate through every entry in the array 
    for ind,val in enumerate(arr):
        if ind <= 1: # then CurMaxM2 does not exist
            CurMaxM2 = float('-inf')
        else:
            CurMaxM2 = CurMax[ind-1] + val
        
        ## calculate the maximum sum
        CurMax.append(max([val, CurMax[-1], CurMaxM2]))
    return CurMax[-1]


#%%
#arr = [-2,1,3,-4,5]
arr = [3,7,4,6,5]

maxSubsetSum(arr)



















