#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 27 14:26:04 2020

@author: hankui

"""


#%%
calorie = [7,4,9,6]

#%%
def marcsCakewalk(calorie):
    ans = 0
    vec = sorted(calorie, reverse=True)
    
    for ind, val in enumerate(vec):
        ans += (2**ind)*val
    return ans


#%%
marcsCakewalk(calorie)