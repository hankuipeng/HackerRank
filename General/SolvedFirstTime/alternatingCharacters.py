# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.

"""


#%% testing cases
#s = 'AAA'
s = 'AAABBABA'


#%%
import collections

def alternatingCharacters(s):
    
    ctr_s = collections.Counter(s)
    Ndel = 0
    
    # if there is only one unique string present
    if len(ctr_s) == 1:
        Ndel = len(s)-1
    else:
        cur = s[0]
        for i in range(1,len(s)):
            if s[i] == cur:
                Ndel += 1
            else:
                cur = s[i]
    return Ndel


#%%
alternatingCharacters(s)