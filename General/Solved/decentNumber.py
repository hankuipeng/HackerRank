#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 26 15:36:47 2020

@author: hankui

"""

# reference: https://codereview.stackexchange.com/questions/54373/sherlock-and-the-beast


#%%
n = 3
n = 5
n = 11


#%% my version 1: this is too slow 
from collections import defaultdict

def decentNumber(n):
    
    ans = -1
    
    n5 = [i for i in range(n+1) if i%3==0] # possible number of 5s
    n3 = [i for i in range(n+1) if i%5==0] # possible number of 3s
    
    lookup = defaultdict(list)
    
    for i,num in enumerate(n3):
        
        needed = n-num
        
        if needed%3 == 0: # if the number of 5s is divisable by 3
            
            ans = max(ans, int('5'*needed+'3'*num))
    
    return ans


#%% one solution 
def decentNumber(n):
    if n % 3 == 0:
        print('5' * n)    
    elif n % 3 == 1 and n >= 10:
        print( '5'* (n - 10) + '3' * (10))
    elif n % 3 == 2 and n >= 5: 
        print('5' *(n - 5) + '3' * (5))
    else:
        print(-1)    
    return


#%% my version 1: this is too slow 
from collections import defaultdict

def decentNumber(n):
    
    ans = -1
    
    n5 = [i for i in range(n+1) if i%3==0] # possible number of 5s
    n3 = [i for i in range(n+1) if i%5==0] # possible number of 3s
    
    lookup = defaultdict(list)
    
    for i,num in enumerate(n3):
        import pdb
        pdb.set_trace()
        needed = n-num # needed number of 5s
        
        if needed in lookup: # if the number of 5s is divisable by 3
            
            ans = max(ans, int('5'*needed+'3'*lookup[needed]))
            
        lookup[needed].append(num)
    return ans










