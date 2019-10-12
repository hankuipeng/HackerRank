#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:31:27 2019

@author: Hankui Peng

"""
    

#%%
from collections import Counter

n = int(input())
s = Counter(map(str, input().split()))

#%% check the first pair manually
count = 0
if s[0] == s[1] and s[0]=='D':
    count = count + 1


#%% sea level is zero after 'sl0' number of steps taken 
sl0 = [0]
sl = 0
for i in range(n):
    if s[i] == 'U':
        sl = sl + 1
    else:
        sl = sl - 1
    
    if sl == 0:
        sl0.append(i+1)


#%%
valleys = 0
for ind in range(len(sl0)-1):
    begin = sl0[ind]
    end = sl0[ind+1]
    count = 0
    if s[begin] == 'D' and s[end-1] == 'U':
            
    #for i in range(begin,end):
    #    if s[i] == 'D' and s[i+1] == 'U':
    #        count = count + 1
    #if count > 0:
        valleys = valleys + 1
            
print(valleys)











