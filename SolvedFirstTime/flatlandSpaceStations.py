#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:44:58 2019

@author: hankui
"""

#%%
c = [0,4]
n = 5

#%%
def flatlandSpaceStations(n, c):
        c_vec = [0 for i in range(n)]
        for ii in range(len(c)):
            c_vec[c[ii]] = 1
        # indices of the space station locations
        inds = [i for i,x in enumerate(c_vec) if x==1]
        
        dists = [0 for i in range(n)];
        for ss in range(n):
            dists[ss] = min([abs(val-ss) for val in inds]);
        print(max(dists))