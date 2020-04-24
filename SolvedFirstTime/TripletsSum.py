#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:17:00 2019

@author: Hankui Peng

"""

# Google topics for interview preparation:
# https://www.geeksforgeeks.org/Google-topics-interview-preparation/
# Find all triplets with zero sum.
# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/


#%% Test input
a = [0, -1, 2, -3, 1]
n = len(a)


#%% function 
def findTriplets(a,n):
    
    pairs = []
    
    # Get all combinations of length 2 with the corresponding indices 
    from itertools import combinations 
    comb = list(combinations(enumerate(a), 2))
    
    # get the combinations and indices separately  
    sumps = [comb[i][0][1] + comb[i][1][1] for i in range(len(comb))]
    indps = [(comb[j][0][0], comb[j][1][0]) for j in range(len(comb))]
    
    logic = []
    for c in range(len(comb)):
        sublist = [element for i, element in enumerate(a) if i not in indps[c]]
        logic.append(-sumps[c] in sublist)
   
    return(sum(logic))


#%%
res = findTriplets(a,n)