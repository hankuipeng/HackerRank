#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:18:02 2019

@author: hankui
"""

#%% a b k
queries = [[1,2,100],[2,5,100],[3,4,100]]
n = 5


#%%
def arrayManipulation(n, queries):
    instance = [0]*n
    nrow = len(queries)
    maxN = 0
    tmp = 0
    for i,vec in enumerate(queries):
        instance[(vec[0]-1):vec[1]] = [x+vec[2] for x in instance[(vec[0]-1):vec[1]]]
        tmp = max(instance)
        if tmp > maxN:
            maxN = tmp
        
    return maxN


#%%
arrayManipulation(n,queries)