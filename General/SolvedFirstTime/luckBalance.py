#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Apr 17 16:42:34 2020

@author: hankui

"""


#%%
def luckBalance(k, contests):
    
    col1 = [contests[i][0] for i in range(len(contests))]
    col2 = [contests[i][1] for i in range(len(contests))]
    
    # indices for important contests
    inds = [ind for ind, val in enumerate(col2) if val>0]
    
    # indices for unimportant contests
    inds2 = [ind for ind, val in enumerate(col2) if val<1]
    
    # lucks for important contests
    vals = [col1[i] for i in inds]
    
    # lucks for losing important contests
    part1 = sum(sorted(vals)[-k:])
    part2 = sum([col1[i] for i in inds2 if col1[i]>0])
    
    # lucks lost for winning contests
    minus = sum(sorted(vals)[:-k])
    
    if k > 0:
        ans = part1+part2-minus
    else:
        ans = -part1 + part2
    return ans


#%%
k = 0
contests = [[5,1], [2,1], [1,1], [8,1], [10,0], [5,0]]

luckBalance(k, contests)