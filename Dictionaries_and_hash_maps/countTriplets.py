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


#%% attempt 1
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


#%% test case 1
arr = [1,3,9,9,27,81]
r = 3


#%% test case 2
arr = [1,5,5,25,125]
r = 5

countTriplets(arr, r)


#%% attempt 2 (2020/05/15)
from collections import Counter 

def countTriplets2(arr, r):
    
    count = 0
    
    st = sorted(list(set(arr))) # the set of unique values
    ctr = Counter(sorted(arr))
    
    #import pdb
    #pdb.set_trace()    
    
    for i in range(len(st)-2):
        if st[i]*r in ctr and st[i]*(r**2) in ctr:
            count += ctr[st[i]] * ctr[st[i]*r] * ctr[st[i]*(r**2)]
    return count


#%% attempt 3 (2020/05/15)
from collections import Counter 
from itertools import combinations

def countTriplets(arr, r):
    
    count = 0
    
    st = sorted(list(set(arr))) # the set of unique values
    ctr = Counter(sorted(arr))
    
    if len(st) <= 2 and r == 1:
        for v in st:
            vec = [v]*ctr[v]
            count += len([v for v in combinations(vec,3)]) 
    else:    
        for i in range(len(st)-2):
            if st[i]*r in ctr and st[i]*(r**2) in ctr:
                count += ctr[st[i]] * ctr[st[i]*r] * ctr[st[i]*(r**2)]
    return count


#%%
arr = [1,1,1,1]
r = 1

st = sorted(list(set(arr))) # the set of unique values
ctr = Counter(sorted(arr))




















