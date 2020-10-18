#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Oct 14 17:46:24 2020

@author: Hankui Peng

"""

# Link to the problem: https://www.hackerrank.com/challenges/separate-the-numbers/problem

s = '99910001001'

# initialisation
loc = 0 # the location of the beginning index of the current number
l = 1 # the length of the current number 
val = s[0] # the initial term 


## Initial check with the feasibility
while (loc-1) <= (len(s)-l):
    
    search_term = str(int(val) + 1)
    
    
    # match the search term with the subsequent sub-string with length l
    if s[(loc+l):(loc+l+len(search_term))] != search_term:
        
        val = s[:(l+1)]
    
    else:
        if loc == 0:
            init = val
        loc += l
        val = search_term
    
    if (loc + l - 1) == len(s):
        ans = 'YES'
        print('YES {}'.format(init))
    else:
        l = len(search_term)