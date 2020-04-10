#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:39:52 2019

@author: Hankui Peng

"""

#%%
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9


#%%

        
#%%
import numpy as np
list = np.unique(ar)
ll = []
for i in range(len(list)):
    item = list[i]
    num = list[i]
    ll_tmp = [i for i,x in enumerate(ar) if x == num]
    ll.append(len(ll_tmp))
    

#%%
#remains = [x % 2 for x in ll]

#%% indices for even numbers in ll
ind = [i for i,x in enumerate(ll) if x%2 == 0]
ans = 0

for l in range(len(ind)):
    ans =+ ll[ind[l]]/2
    


#%% solution
from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0

for x in c:
    ans += c[x] // 2
    
print(ans)

