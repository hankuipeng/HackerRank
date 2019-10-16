#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:13:04 2019

@author: hankui
"""

#%%
s = 'ifailuhkqq'
#s = 'kkkk'


#%%
def sherlockAndAnagrams(s):
    count = 0
    n = len(s)
    for l in range(n):
        dic = [] # the dictionary of all different combinations
        for loc in range(n-l):
            if Counter(s[loc:loc+l+1]) not in dic:
                dic.append(Counter(s[loc:loc+l+1])) # to be compared to
            dic
        print(dic)
        
#%%
from collections import Counter
from itertools import combinations

def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j     in b]))
    return sum(count)


#%%
from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    import pdb; pdb.set_trace()
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)


