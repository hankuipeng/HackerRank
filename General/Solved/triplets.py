#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:34:54 2020

@author: hankui
"""


#%% attempt 1
from collections import defaultdict

def triplets(a, b, c):
    
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    ans = 0
    #pos = defaultdict(list)  
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    for ind,val in enumerate(b):
        
        ai = len([v for v in a if v<=val])
        ci = len([v for v in c if v<=val])
        
        ans += ai*ci
        
    return ans


#%% my final submission that passed all tests
def triplets(a, b, c):
    
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    ans = 0
    ai = 0
    ci = 0
    #pos = defaultdict(list)  
    
    for ind,val in enumerate(b):

        while ai < len(a) and a[ai] <= val:
            ai += 1
        
        while ci < len(c) and c[ci] <= val:
            ci += 1
        
        ans += ai*ci
        
    return ans


#%% one solution
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    ans = 0
    
    while bi < len(b):
        
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    
    return ans

#%%
a = [1,4,5]
b = [2,3,3]
c = [1,2,3]


#%%
triplets(a,b,c)