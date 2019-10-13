#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:50:59 2019

@author: hankui
"""

#%%
5 % 3 # obtain the remainder



#%%
magazine = 'give me one grand todays night'.split()
note = 'give one grand today'.split()


#%%
def checkMagazine(magazine, note):
    Mag = magazine.split()
    Not = note.split()
    ans = 'Yes'
    for i,val in enumerate(Not):
        if val in Mag:
            ind = Mag.index(val) # location in the magazine
            Mag[ind] = []
        else:
            ans = 'No'
    return ans

#%% 
from collections import Counter

def ransom_note(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print('Yes')
    else:
        print('No')