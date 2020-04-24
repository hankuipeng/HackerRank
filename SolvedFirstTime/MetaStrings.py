#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:32:30 2019

@author: hankui
"""

#%% check if two strings can become the same after a swap of one string
# https://www.geeksforgeeks.org/meta-strings-check-two-strings-can-become-swap-one-string/

str1 = 's'
str2 = 's'


#%%
for _ in range(int(input())):
    
    #ans = 0
    
    str1 = list(map(str,input().split()))
    
    str2 = list(map(str,input().split()))
    
    # if two strings are not of the same lengths
    if len(str1[0]) != len(str2[0]):
        ans = 0
        print(ans)
    else:
        bools = []
        for i in range(len(str1[0])):
            
            bools.append(str1[0][i] == str2[0][i])
            
        if sum(bools) == (len(str1[0])-2):
            ans = 1
        elif sum(bools) != (len(str1[0])-2):
            ans = 0
        print(ans)

