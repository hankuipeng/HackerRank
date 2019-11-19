#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:34:03 2019

@author: hankui
"""

#%%
s2 = 'SHINCHAN'
s1 = 'NNHARAAA'
#s1 = 'OUDFRMYMAW'
#s2 = 'AWHYFCCMQX'
#s1 = 'AA'
#s2 = 'BB'
#s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
#s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'


#%% version 1 (with bugs)
def commonChild(s1, s2):
    ans = 0
    ind2 = -1
    for val_i in s1:
        if val_i in s2:
            cur = s2.index(val_i)
            #ind2 = s2.index(val_i)
            if cur > ind2:
                ans += 1
                ind2 = cur
    return ans


#%% version 2
def commonChild(s1, s2):
    import pdb; pdb.set_trace()
    ans = 0
    ind2 = -1

    if len([v for v in s1 if v in s2]) > 0:
        s1f = s1.index([v for v in s1 if v in s2][0])
        s2f = s2.index([v for v in s2 if v in s1][0])
        if s1f > s2f:
            copy = s1
            s1 = s2
            s2 = copy
        
    for val_i in s1:
        if val_i in s2:
            #indices = [s2.index(v) for v in s2 if v in s2]
            #letters = [v for v in s1 if v in s2]
            cur_list =[i for i, ltr in enumerate(s2) if ltr == val_i]
            cur_01 = [val>ind2 for val in cur_list]
            if sum(cur_01)>0:
                cur = cur_list[cur_01.index(True)]
                #cur = s2.index(val_i)
                #ind2 = s2.index(val_i)
            if cur > ind2:
                ans += 1
                ind2 = cur
    return ans

#%%
ans = 0
ind2 = -1
i = 0
cur = -1
#%%
indices = [s2.index(v) for v in s1 if v in s2[(ind2+1):]]
#letters = [v for v in s1 if v in s2]

#%%

while True:
    import pdb; pdb.set_trace()
    new_s2 = s2[(cur+1):]
    new_ind0 = [new_s2.index(v) for v in s1[i:] if v in new_s2]
    new_ind = [val+cur+1 for val in new_ind0]
    indices = new_ind
    if len(indices) == 0:
        break
    #print(ans)
    cur_01 = [val>ind2 for val in indices]

#if sum(cur_01)>0:
    cur = min(indices)
    ans += 1
    ind2 = cur
    i +=1
    


