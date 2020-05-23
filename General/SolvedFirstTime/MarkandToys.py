#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:07:31 2019

@author: hankui
"""


#%%
k = 50
nk = [1, 12, 5, 111, 200, 1000, 10]


#%%
ord_vec = sorted(nk)

cur_sum = 0
count = 0
for i in range(len(nk)):
    cur_sum += ord_vec[i]
    count += 1
    if cur_sum > k:
        break

ord_vec[:count-1]