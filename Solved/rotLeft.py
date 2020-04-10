#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:59:29 2019

@author: hankui
"""

#%%
a = [1,2,3,4,5]
d = 4

#%%
def rotLeft(a, d):
    tmp = a[d:] + a[:d]
    res = [int(i) for i in tmp.split()]
    print(res)
    return res