#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May 17 20:15:25 2020

@author: hankui

"""


#%%
from collections import Counter
def anagram(s):
    
    if len(s)%2 != 0:
        ans = -1
    else:
        #import pdb
        #pdb.set_trace()
        l = len(s)//2
        
        s1 = s[:l]
        s2 = s[l:]
        
        ctr1 = Counter(s1)
        ctr2 = Counter(s2)
        
        diff = ctr1 - ctr2
        
        ans = sum([diff[v] for v in diff])
    return ans


#%%
s = 'xaxbbbxx'
#s = 'aaabbb'
anagram(s)


#%%
ctr1 = Counter(s1)
ctr2 = Counter(s2)