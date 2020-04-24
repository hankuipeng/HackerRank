#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Apr 24 10:54:19 2020

@author: hankui

"""


#%%
#from itertools import combinations
cost = [2,2,4,3]
money = 4

#ans_li = []
# step 1: rule out the indices whose values are greater than 'money'
new_tu = [(val,ind) for ind,val in enumerate(cost) if val < money]

new_li = [v[0] for v in new_tu]


#%%
for pairs in combinations(new_tu, 2):
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    if pairs[0][0] + pairs[1][0] == money:
        #ans_vals = [min(pairs), max(pairs)]
        ans_li = [pairs[0][1]+1, pairs[1][1]+1].sort()
#a = [entry[1] for entry in new_tu if entry[0] == ans_vals[0]][0]
#b = [entry[1] for entry in new_tu if entry[0] == ans_vals[1]][0]

print(' '.join(map(str, ans_li)))


#%%

from collections import defaultdict

# Returns the indices of two numbers that add up to the target
def two_sums(nums, target):

    lookup = defaultdict(list)
    
    #import pdb
    #pdb.set_trace()    
    
    for i, num in enumerate(nums):
        
        needed = target - num
        
        if needed in lookup:
            
            return [lookup[needed][0]+1, i+1]
        
        lookup[num].append(i)

    return None