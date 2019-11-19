#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:11:27 2019

@author: hankui
"""

N = 5
S = 15
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#%%
#code

for _ in range(int(input())):
    line1 = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    
    N = line1[0]
    S = line1[1]
    
    import numpy as np

    sums = []
    l_ind = []
    i_ind = []
    for l in range(N):
        length = l+1
        for i in range(N-l):
            l_ind.append(l)
            i_ind.append(i)
            sums.append(sum(arr[i:(i+length)]))
            
    if (S in sums):
        # ind = sums.index(S)
        inds = [i for i,x in enumerate(sums) if x==S]
        i_inds = [i_ind[i[1]] for i in enumerate(inds)]
        
        min_index = i_inds.index(min(i_inds))
        min_value = min(i_inds)
        
        ind = inds[min_index]
        
        length = l_ind[ind]+1
        i = min_value
        ans = [(i+1),(i+length)]
        for item in ans:
            print(item, end=' ')
        print()
    
    elif (S not in sums):
        print(-1)