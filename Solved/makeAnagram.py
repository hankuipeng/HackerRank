#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Apr 10 11:33:23 2020

@author: hankui

"""


#%% Print a single integer denoting the number of characters you must delete 
# to make the two strings anagrams of each other.
import collections 

def makeAnagram(a, b):

    # count the lengths of both strings
    len_a, len_b = len(a), len(b)
    
    # count the frequencies of each unique entry in each string
    ctr_a = collections.Counter(a)
    ctr_b = collections.Counter(b)
    
    # count the number of strings that can be matched
    intersect = set(a).intersection(set(b))
    count = 0
    for val in intersect:
        num = min(ctr_a[val], ctr_b[val])
        count += num
    
    # calculate the number of deletions needed
    num_del = len_a + len_b - count*2 
    
    return num_del 


#%% testing 
a = 'aabcdde'
b = 'acdefg'
makeAnagram(a, b)