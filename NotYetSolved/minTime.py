#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Apr 29 18:14:51 2020

@author: hankui

"""


#%% test case 1
n = 3 
goal = 10
machines = [1, 3, 4]
# ans = 7


#%% test case 2
goal = 5
machines = [2,3]


#%% test case 3
goal = 56
machines = [63, 2, 26, 59, 16, 55, 99, 21, 98, 65]


#%% attempt 1
def minTime1(machines, goal):
#    ans = 0
    num = 0
    day = 1
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    while num < goal: 
        num = 0
        # num: number of items produced so far
        for i in range(len(machines)):
            num += day//machines[i]
        day += 1
    return day-1


#%% attempt 2
def minTime(machines, goal):
    
    # calculate the number of units that can be produced in one day 
    num = sum([1/v for v in machines])
    ans = goal//num
    
    # need to remove the machines whose values are greater than ans
    new = [v for v in machines if v <=ans]
    
    if num*ans >= goal:
        pass
    else:
        ans += 1
    return int(ans)


#%% attempt 3
from functools import reduce
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def minTime(goal, machines):
    
    n_days = lcmm(*machines) # the least number of days for all machines to have produced integer number of items
    
    n_items = sum([n_days/v for v in machines])
    
    n0 = goal//(n_items/n_days)
    
    # number of items produced in n0 days
    n = sum([n0//v for v in machines])
    
    while n < goal:
        n0 += 1
        n = sum([n0//v for v in machines])
    
    return n0


#%%
minTime(machines, goal)
