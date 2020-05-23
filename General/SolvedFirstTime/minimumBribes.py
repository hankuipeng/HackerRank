#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:33:23 2019

@author: hankui
"""

#%%
n = 5
#q = [2, 1, 5, 3, 4]
#q = [2, 5, 1, 3, 4]


#%%
# caveat: although one person can only bribe at most 2 people, the person can however
# be bribed multiple times 
def minimumBribes(q):
    n = len(q)
    ans = 0
    # too chaotic situation
    if q[0] > 3 or q[1] > 4 or q[n-2] < (n-3) or q[n-1] < (n-2):
        ans = 'Too chaotic'
    # not too chaotic situation
    else:
        i = 0
        while i < (n-1):
            if abs(q[i]-(i+1)) == 1:
                ans = ans + 1
                i = i + 2
                import pdb; pdb.set_trace()
            if abs(q[i]-(i+1)) == 2:
                copy = q[i]
                q[i] = q[i+2]
                q[i+2] = copy
                ans = ans + 1
    return ans 


#%%
minimumBribes(q)






