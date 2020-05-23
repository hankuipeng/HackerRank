#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 18 12:10:28 2020

@author: hankui

"""


#%% 
import itertools

def maximumPerimeterTriangle(sticks):
    
    n = len(sticks)
    ans = [-1]
    
    if n == 1:
        if sticks[0] + sticks[1] > sticks[2] and abs(sticks[0] - sticks[1]) < sticks[2]:
            ans = sticks
        else:
            ans = [-1]
    
    else:
        cur_max = -1
        valid_list = []
        for comb in itertools.combinations(sticks, 3):
            if comb[0] + comb[1] > comb[2] and abs(comb[0] - comb[1]) < comb[2]:
                cur = sorted(list(comb))
                valid_list.append(cur)
                if sum(cur) > cur_max:
                    cur_max = sum(cur)
        
# =============================================================================
#         import pdb
#         pdb.set_trace()
# =============================================================================
        
        if len(valid_list) == 0:
            ans = [-1]
        if len(valid_list) == 1:
            ans = valid_list[0]
        if len(valid_list) > 1:
            mm_tp = [(max(val),min(val),ind) for ind,val in enumerate(valid_list)]
            std = sorted(mm_tp, key=lambda tup: (tup[0],tup[1]) , reverse=True)
            ans = valid_list[std[0][2]]
    return ans   


#%% 
sticks = [1, 2, 3, 4, 5]


#%%
maximumPerimeterTriangle(sticks)


#%%
max_li = [5,5,3,4,1]
min_li = [2,3,1,1,1]

