#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:51:23 2019

@author: hankui
"""

#%%
s1 = 'he'
s2 = 'world'

#%%
s1 = 'wouldyoulikefries'
s2 = 'abcabcabcabcabcabc'


#%% first attempt
from collections import Counter
def twoStrings(s1, s2):
    if Counter(s2) - Counter(s1) == Counter(s2):
        ans = 'NO'
    else:
        ans = 'YES'
    return ans


#%% attempt 2 (2020/05/15)
def twoStrings(s1, s2):
    
    ans = 'NO'
    in_dict = {}
    for i,v in enumerate(s1):
        in_dict[v] = i
    for i,v in enumerate(s2):
        if v in in_dict:
            ans = 'YES'
            break
    return print(ans) 