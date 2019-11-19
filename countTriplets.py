#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:33:21 2019

@author: hankui
"""

#%%
#r = 5
#arr = [1, 5, 5, 25, 125]
r = 2
#arr = [1,2,1,2,4]
arr = [1,2,4]

#%%
from collections import Counter
def countTriplets(arr, r):
    count = 0
    n = len(arr)
    ct = Counter(arr)
    ct_vals = [i for i in ct]
    if len(ct_vals) == 1 and r == 1:
        count = int(n*(n-1)*(n-2)/6)
    else:
        for i in range(len(ct_vals)-2):
            count += ct[ct_vals[i]]*ct[ct_vals[i+1]]*ct[ct_vals[i+2]]
    return count 


#%%
from collections import Counter

def countTriplets(arr, r):
    import pdb; pdb.set_trace()
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1

    return count








