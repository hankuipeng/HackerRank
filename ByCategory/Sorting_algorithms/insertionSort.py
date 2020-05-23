#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat May 23 10:42:37 2020

@author: hankui

"""

# https://www.hackerrank.com/challenges/insertionsort2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#%%
def insertionSort1(n, arr):
    insert_v = arr[-1]
    vec = arr[:-1]
    vec_cur = vec
    ind = 0
    
    #import pdb
    #pdb.set_trace()
    
    for i in range(len(vec)):
        vec1 = vec.copy()
        if vec[-(i+1)] > insert_v:
            vec1.insert(-(i+1), vec[-(i+1)])
            #print(' '.join(map(str, vec1)))
            ind = -(i+1)
            vec_cur = vec1
    if (n+ind-1) == len(vec_cur):
        vec_cur.append(insert_v)
    else:
        vec_cur[n+ind-1] = insert_v
    # print(' '.join(map(str, vec_cur)))
    return vec_cur

#%%
arr = [1,4,3,5,6,2]
n = len(arr)
insertionSort1(n, arr)


#%%
def insertionSort2(n, arr):
    
    # print(' '.join(map(str, arr)))
    
    for i in range(1, n):
        #import pdb
        #pdb.set_trace()
        
        vec = arr[:i+1]    
        l = len(vec)
        part1 = insertionSort1(l, vec)
        part1.extend(arr[i+1:])  
        arr = part1.copy()
        print(' '.join(map(str, arr)))


#%%
insertionSort2(n, arr)

