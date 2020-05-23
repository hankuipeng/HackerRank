#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May 20 22:20:36 2020

@author: hankui

"""


#%% references:
# https://brilliant.org/wiki/sorting-algorithms/


#%%
def maximumToys(prices, k):
    
    ord_vec = sorted(prices)

    cur_sum = 0
    count = 0
    for i in range(len(prices)):
        cur_sum += ord_vec[i]
        count += 1
        if cur_sum > k:
            break

    return count-1


