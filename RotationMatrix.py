#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:39:41 2019

@author: hankui
"""
# source: https://practice.geeksforgeeks.org/problems/rotate-by-90-degree/0
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
   
    if (n > 0):
        
        rows = list()
        for i in range(n):
            rows.append(arr[(i*n):(i*n+n)])
        
        #%%
        verticals = list()
        for i in range(n):
            verticals.append(rows[i][::-1])
            
        
        #%%
        ans = list()
        for i in range(n):
            for j in range(n):
                ans.append(verticals[j][i])
        for item in ans:
            print(item, end=' ')
        print()
    