#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 22:27:55 2019

@author: hankui
"""

#%% 

# https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary/0
dictionary = ['lr', 'm', 'lrm', 'hcdar', 'wk']
string = 'hcdarlrm'


#%%
n = len(dictionary)
from numpy import zeros
indicator = zeros([1,n])

for d in range(len(dictionary)):
    count = 0
    for iter in range(len(dictionary[d])):
        if dictionary[d][iter] in string[0]:
            count += 1
    if count == len(dictionary[d]):
        indicator[0,d] = 1

#%%
lengths = []
for l in range(len(dictionary)):
    lengths.append(len(dictionary[l]))
    
for j in range(len(dictionary)):
    if indicator[0,j] == 0:
        lengths[j] = 0

#%%
max_ind = lengths.index(max(lengths))
ans = dictionary[max_ind]
ans


#%%
ind = np.array(indicator[0,:]>0, dtype = bool)

from itertools import compress

list(compress(lengths, ind))