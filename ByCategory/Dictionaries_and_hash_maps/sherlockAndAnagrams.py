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
def sherlockAndAnagrams0(s):
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

def sherlockAndAnagrams1(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j     in b]))
    return sum(count)


#%% attempt 1
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


#%% attempt 2 (2020/05/15)
from collections import Counter

def sherlockAndAnagrams(s):
    
    substr = []
    count = 0
    
    for l in range(1, len(s)): # list all possible substrings with length l
    
        counter_li = []
        #import pdb
        #pdb.set_trace()
        
        for ind in range(len(s)-l+1): 
            
            substr.append(s[ind:ind+l])
            
            curCounter = Counter(substr[-1])
            
            cc = len([v for v in counter_li if curCounter == v])
            count += cc
            
            counter_li.append(curCounter)
        
    
    return count 


#%% test case
s = 'abba'   
#s = 'kkkk'
sherlockAndAnagrams(s)