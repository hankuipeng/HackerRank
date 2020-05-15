#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon May 11 13:58:29 2020

@author: hankui

"""


#%%
def viralAdvertising(n):
    
    ans = 2 # end of day 1
    curNum = 2
    i = 1 # counter for day
    
    #import pdb
    #pdb.set_trace()
    
    while i < n:
        i += 1
        curNum = (curNum*3)//2
        ans += curNum
    return ans 


#%%
viralAdvertising(3)