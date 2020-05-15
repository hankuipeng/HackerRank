#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:00:06 2020

@author: hankui
"""


#%%
def stepPerms0(n):
    #import pdb
    #pdb.set_trace()
    if n == 1:
        ans = 1
    if n == 2:
        ans = 2
    if n == 3:
        ans = 4
    if n >= 4:
        ans = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return ans 


#%%
def stepPerms(n):
    li = [1,2,4]
    if n <= 3:
        ans = li[n-1]
    else:
        #import pdb
        #pdb.set_trace()
        i = 3
        while i < n:
            i += 1
            li[0],li[1],li[2] = li[1], li[2], sum(li)
        ans = li[-1]
    return ans


#%%
stepPerms(4)

