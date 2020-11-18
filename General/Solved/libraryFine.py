#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Nov 18 10:17:23 2020

@author: Hankui Peng

"""

# Link to question: https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2: # late return by calendar year
        cost = 10000
    elif y1 < y2: # early return by calendar year
        cost = 0
    else:  
        if m1 > m2: # late return by month
            cost = 500 * (m1 - m2)
        elif m1 < m2: # early return by month
            cost = 0
        else: 
            if d1 > d2: # late return by day
                cost = 15 * (d1 - d2)
            else:
                cost = 0
    return cost