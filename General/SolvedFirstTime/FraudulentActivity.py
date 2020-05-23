#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 23:08:47 2019

@author: hankui
"""


#%%
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5


#%%
expenditure = [1, 2, 3, 4, 4]
d = 4


#%%
expenditure = [10, 20, 30, 40, 50]
d = 3


#%%
count = 0
for loc in range(d,len(expenditure)):
    #import pdb
    #pdb.set_trace()
    arr = expenditure[loc-d:loc]
    
    # first: order the sequence of expenditures
    ord_arr = sorted(arr) 
    
    # then: find the median
    if len(ord_arr) % 2 == 0: # if the length is even
        med = (ord_arr[len(ord_arr)/2-1]+ord_arr[len(ord_arr)/2])/2
    else:
        med = ord_arr[len(ord_arr)//2]
    
    # finally: compare loc to 2*median
    if loc >= 2*med:
        count += 1


#%% this is not fast enough...
count = 0
if d % 2 == 0: # if the length is even
    #import pdb
    #pdb.set_trace()
    for loc in range(d,len(expenditure)):
        arr = expenditure[loc-d:loc]
    
        # first: order the sequence of expenditures
        ord_arr = sorted(arr) 
    
        med = (ord_arr[int(len(ord_arr)/2-1)]+ord_arr[int(len(ord_arr)/2)])/2
        
        # finally: compare loc to 2*median
        if expenditure[loc] >= 2*med:
            count += 1
else:
    for loc in range(d,len(expenditure)):
        #import pdb
        #pdb.set_trace()
        arr = expenditure[loc-d:loc]
    
        # first: order the sequence of expenditures
        ord_arr = sorted(arr) 
    
        med = ord_arr[len(ord_arr)//2]
        
        # finally: compare loc to 2*median
        if expenditure[loc] >= 2*med:
            count += 1


#%%
from bisect import insort, bisect_left
def activityNotifications(expenditure, d):
    import pdb
    pdb.set_trace()
    v = sorted(expenditure[: d])
    count = 0
    for i, current in enumerate(expenditure[d:]):
        de = expenditure[i]
        if d%2 == 0:
            if current >= v[d//2] + v[d//2-1]:
                count += 1
        elif current >= v[d//2]*2:
                count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
    return count



