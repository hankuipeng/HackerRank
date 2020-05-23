#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:08:10 2019

@author: hankui
"""


#%%
import sys
 
while True:
    try:
        num = sys.stdin.readline()
 
        array = []
 
        for i in range(0, int(num)):
            a = sys.stdin.readline()
            array.append(int(a))
 
        b = set(array)
        c = list(b)
        d = sorted(c)
 
        for i in range(len(d)):
            print(d[i])
    except:
        break

