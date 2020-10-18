#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 12 20:22:22 2020

@author: Hankui Peng

"""

# Link to question: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

from string import ascii_lowercase

[ascii_lowercase[i] for i in range(26)]


#%%
s = 'abccddde'
queries = [6, 1, 3, 12, 5, 9, 10]


#%%
import string
from collections import Counter

unif_strs = {}
count = 1

for i,v in enumerate(s):
    
    if v not in unif_strs:
        unif_strs[v] = string.ascii_lowercase.index(v) + 1
        count = 1
        
    elif v == s[i-1]:
        count += 1
        unif_strs[v*count] = (string.ascii_lowercase.index(v) + 1)*count

counts = [unif_strs[v] for v in unif_strs]

counts_dict = Counter(counts)

for num in queries:
    if num in counts_dict:
        print('YES')
    else:
        print('NO')

