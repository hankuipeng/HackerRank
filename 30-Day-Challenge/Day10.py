#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:36:45 2019

@author: Hankui Peng

"""

#%%


#%%
n=439
br = bin(n)[2:]
count = 0
pre = 1

for curr_val in br:
    if int(curr_val) == 1 and int(pre) == 1:
        count += 1
        pre = curr_val
        curr_max = max(curr_max, count)
    else:
        curr_max = max(curr_max, count)
        count = 0
        count += int(curr_val)
        pre = int(curr_val)

print(curr_max)