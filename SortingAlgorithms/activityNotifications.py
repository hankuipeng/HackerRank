#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:34:30 2020

@author: hankui
"""


#%%
from bisect import insort, bisect_left

def activityNotifications(expenditure, d):

    v = sorted(expenditure[: d])
    count = 0

    import pdb
    pdb.set_trace()
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


#%%
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

activityNotifications(expenditure, d)