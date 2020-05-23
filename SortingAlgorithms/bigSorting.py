#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May 20 23:28:20 2020

@author: hankui

"""


#%% attempt 1
def bigSorting(unsorted):
    arr = [int(v) for v in unsorted]
    sorted_arr = sorted(arr)
    return [str(v) for v in sorted_arr]


#%% someone's solution
def bigSorting(unsorted):
    return sorted(unsorted,key=int)


#%% one solution (that passed all the checks)
def bigSorting(unsorted):
    return sorted(sorted(unsorted), key=len)