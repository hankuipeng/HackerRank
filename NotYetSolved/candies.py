#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 19 18:44:07 2020

@author: hankui

"""


#%%
def candies0(n, arr):
    
    rewards = [1]*n
    
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            rewards[i] = rewards[i-1] + 1
    
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            if rewards[i] <= rewards[i+1]:
                rewards[i] = rewards[i+1] + 1
    
    return sum(rewards), rewards


#%%
# import numpy as np
def candies(n, arr):
    
    rewards = [0]*n
    uniq_vals = list(set(arr))
    
    inds = [ind for ind,val in enumerate(arr) if val==uniq_vals[0]]
    for ind in inds:
        rewards[ind] = 1
    
    for i in range(1,len(uniq_vals)):
        inds = [ind for ind,val in enumerate(arr) if val==uniq_vals[i]]
        for v in inds:
            if v == 0: # the index is at the lower end of the array 
                # if the right side is smaller than it
                if arr[v+1] < arr[v]:
                    rewards[v] = rewards[v+1] + 1
                
                # if the right side is larger than it
                if arr[v+1] >= arr[v]:
                    rewards[v] = max([1, rewards[v]])
            
            if v == n-1: # the index is at the upper end of the array 
                # if the left side is smaller than it 
                if arr[v-1] < arr[v]:
                    rewards[v] = rewards[v-1] + 1
                
                # if the left side is larger than it 
                if arr[v-1] >= arr[v]:
                    rewards[v] = max([1, rewards[v]])
                
            if v > 0 and v < n-1: # the index is not at either end of the array 
                # if only left side is smaller than it
                if arr[v-1] < arr[v] and arr[v+1]>=arr[v]:
                    rewards[v] = rewards[v-1] + 1
                    
                # if only right side is smaller than it 
                if arr[v+1] < arr[v] and arr[v-1]>=arr[v]:
                    rewards[v] = rewards[v+1] + 1
                    
                # if both sides are smaller than it
                if arr[v+1] < arr[v] and arr[v-1] < arr[v]:
                    rewards[v] += max([rewards[v-1], rewards[v+1]]) + 1
                
                # if both sides are larger than it
                if arr[v+1] >= arr[v] and arr[v-1] >= arr[v]:
                    rewards[v] = max([1, rewards[v]])
            
    return sum(rewards), rewards


#%%
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
n = len(arr)

num, rewards = candies(n, arr)