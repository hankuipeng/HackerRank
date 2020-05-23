#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri May 15 10:43:49 2020

@author: hankui
"""

#%%
def checkMagazine0(magazine, note):
    
    ans = 'Yes'
    
    inp = magazine.split(' ') # input list of strings
    out = note.split(' ') # the list of strings to be matched
    
    inp_dict = {}
    for i in range(len(inp)):
        inp_dict[inp[i]] = i
    
    #import pdb
    #pdb.set_trace()
    # check if every element of out can be found in inp_dict
    for i,v in enumerate(out):
        if v not in inp_dict:
            ans = 'No'
            break
    return ans


#%%
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print('Yes')
    else:
        print('No')


#%% test case 1
magazine = 'give me one grand today night'
note = 'give onee grand today'

checkMagazine(magazine, note)