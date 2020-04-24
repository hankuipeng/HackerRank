#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Apr 15 13:20:02 2020

@author: hankui

"""


#%% the case where substrings do not have to be connected
# =============================================================================
# import collections
# 
# def substrCount(n, s):
#     
#     ctr = collections.Counter(test_str)
#     n_unique = len(ctr) # the number of unique letters 
#     
#     import pdb
#     pdb.set_trace()
#     
#     # count for scenario 1
#     count = sum([ctr[val] for val in ctr])
#     
#     # count for scenario 2
#     for val in ctr:
#         if ctr[val] > 1:
#             count += (ctr[val]//2)*(n_unique-1)
#             
#     return count
# 
# =============================================================================

#%% the case where substrings do have to be connected
# The following function timed out 
import collections

def substrCount(n, s):
    
    count = n
    
    for l in range(2, n+1): # length of the substring
        
        for j in range(0,n-l+1): # the index of the beginning of the substring 
            
            substr = s[j:j+l]
            ctr = collections.Counter(substr)
            
            if l % 2 == 0:
                if len(ctr) == 1:
                    count += 1
            else:
                subsub_ctr = collections.Counter(substr[:l//2]+substr[l//2+1:])
                
                if len(ctr) == 1: # if all letters are the same 
                    count += 1
                if len(subsub_ctr) == 1 and len(ctr) > 1:
                    count += 1
    return count


#%% one solution
def substrCount(n, s):
    
    prevChar = s[0]
    count = 1
    allChars = []
    res = 0 

    for c in s[1:]:
        if (c == prevChar):
            count += 1
        else:
            allChars.append((prevChar, count))
            res += ((count) * (count + 1)) // 2
            count = 1
            prevChar = c
    
    allChars.append((prevChar, count))
    res += ((count) * (count + 1)) // 2

    for i, val in enumerate(allChars[1:len(allChars)-1], start=1):
        left, right = allChars[i-1], allChars[i+1]
        if ((val[1] == 1) and (left[0] == right[0])):
            res += min(left[1], right[1])
            
    return res
#%%
# test_str = 'abbccdde'
# test_str = 'abcbaba'
test_str = 'aaaa'
substrCount(len(test_str), test_str)


#%%
[test_str[i: j] for i in range(len(test_str)) 
          for j in range(i + 1, len(test_str) + 1)] 