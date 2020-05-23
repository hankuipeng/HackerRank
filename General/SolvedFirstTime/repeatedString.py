#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:17:14 2019

@author: hankui
"""

#%%
s = 'ababc'
n = 10


#%%
def repeatedString(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count = count + 1
    if n > len(s):
        rpt = (n // len(s))
        count = count * rpt
        remains = n % len(s)
        if remains > 0:
            for i in range(remains):
                if s[i] == 'a':
                    count = count + 1
    else:
        count = 0
        for i in range(n):
            if s[i] == 'a':
                count = count + 1
    return count