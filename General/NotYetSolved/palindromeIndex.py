#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May 17 17:20:17 2020

@author: hankui
"""


#%%
def palindromeIndex0(s):
    
    ans = -1
    
    # if it is not a palindrome already then we proceed
    if s[::-1] != s:
        for i in range(len(s)):
            
            s1 = s[:i]+s[i+1:]
            re = s1[::-1]
            l = len(s1)//2
            
            if re[:l] == s1[:l]:
                ans = i
                break
    return ans


#%% attempt 2
def palindromeIndex2(s):
    
    ans = -1
    
    # if it is not a palindrome already then we proceed
    if s[::-1] != s:
        for i in range(len(s)):
            #import pdb
            #pdb.set_trace()
            s1 = s[:i]+s[i+1:]
            l = len(s1)//2
            if len(s1)%2 == 0:
                half_s1 = s1[l:]
            else:
                half_s1 = s1[l+1:]
            re = half_s1[::-1]
            
            if re == s1[:l]:
                ans = i
                break
    return ans


#%% one solution (posted by someone)
def palindromeIndex(s):
    N = len(s)
    N_i = N - 1
    s_i = s[::-1]
    if s == s_i:
            return -1

    for i in range(N):
            test = s[:i] + s[i+1:]
            test_i = s_i[:N_i-i] + s_i[N_i-i+1:]
            if test == test_i:
                    return i

    return -1


#%% test case
s = 'aaab'
s = 'baa'
palindromeIndex(s)


#%%
