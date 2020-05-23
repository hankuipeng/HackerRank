#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May 17 19:35:42 2020

@author: hankui

"""

# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


#%% my attempt (2020/05/17)
def commonChild1(s1, s2):
    
    nc = len(s1) + 1 # number of rows 
    nr = len(s2) + 1 # number of columns
    
    # construct the dynamic programming table
    dp = [[0]*nr for _ in range(nc)]
    
    # build the DP table
    nr = len(s1) + 1
    nc = len(s2) + 1
    dp = [[0]*nc for _ in range(nr)]
    
    
    for i in range(1,nr):
        for j in range(1,nc):
            #import pdb
            #pdb.set_trace()
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
    return dp[nr-1][nc-1]


#%% one solution (posted by someone)
def commonChild(s1, s2):
    
    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)

    for r in s1:
        
        # import pdb
        # pdb.set_trace()
        
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr,prev

    return prev[-1]


#%%
s1 = 'acbcf'
s2 = 'abcdaf'

commonChild(s1, s2)








