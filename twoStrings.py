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


#%%
from collections import Counter
def twoStrings(s1, s2):
    if Counter(s2) - Counter(s1) == Counter(s2):
        ans = 'NO'
    else:
        ans = 'YES'
    return ans