#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:48:33 2020

@author: hankui
"""


#%%
# w = [16, 18, 10, 13, 2, 9, 17, 17, 0, 19]

w = [1, 2, 3, 21, 7, 12, 14, 21]


#%%
def toys(w):
    n = 1
    w.sort()
    counter = min(w)+4
    import pdb
    pdb.set_trace()
    for ind, val in enumerate(w):
        if val <= counter:
            pass 
        else:
            n += 1
            counter = val + 4
    return n

#%%
toys(w)