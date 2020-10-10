#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct  3 20:59:36 2020

@author: hankui

"""


#%%
def funnyString(s):
    
    ans = 'Funny'
    
    num_s = [ord(v) for v in s]
    num_s_rev = num_s[::-1]
    
    
    return ans 


#%%
s = 'acxz'
#s = 'bcxz'
#s = 'ivvkx'

num_s = [ord(v) for v in s]
num_s_rev = num_s[::-1]

ans = 'Funny'

for i in range(1, len(s)):
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    diff = abs(num_s[i] - num_s[i-1])
    
    diff_rev = abs(num_s_rev[i] - num_s_rev[i-1])
    
    if diff != diff_rev:
        
        ans = 'Not Funny'
    
        break