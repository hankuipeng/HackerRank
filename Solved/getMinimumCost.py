#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr 28 20:25:31 2020

@author: hankui

"""

## greedy florist 


#%%
def getMinimumCost(k, c):
    
    # if the number of friends is the same as the #. of types of flowers
    if len(c) == k:
        ans = sum(c)
    
    ord_c = sorted(c, reverse=True) # sort the costs in ascending order 
    
    # if the number of friends is more than the different types of flowers
    if len(c) < k:
        part1 = sum(c)
        part2 = ord_c[-1]*(k-len(c))
        ans = part1+part2
        
    # if the number of friends is less than the different types of flowers
# =============================================================================
#     if len(c) > k:
#         
#         part1 = sum(ord_c[:k]) 
#         
#         # number of flowers left to be bought
#         r = len(c) - k
#         
#         if r <= k:
#             part2 = sum([ord_c[i]*2 for i in range(k, len(c))])
#             
#         ans = part1+ part2
# =============================================================================
    
    if len(c)//k >= 1:
        ans = 0
# =============================================================================
#         import pdb
#         pdb.set_trace()
# =============================================================================
        for i in range(1,len(c)//k+1):
            ans += sum(ord_c[(i-1)*k:k*i])*i
        if len(c)%k != 0:        
            ans += sum(ord_c[-(len(c)%k):])*(len(c)//k+1)
    return ans


#%%
getMinimumCost(k, c)


#%% test case 1
k = 3
c = [6,2,5]


#%% test case 2
k = 3
c = [1, 3, 5, 7, 9]
ord_c = sorted(c, reverse=True)


#%% test case 3
str_c = '120854 100862 523789 849072 23733 355147 660925 59103 801528 607947 51312 754005 823629 876280 23088 668838 214629 641310 66064 541147 97284 579336 319949 193067 35064 227785 376976 146458 258150 551784 961936 189099 552128 318057 39381 41667 316754 680180 681303 7132 472252 791845 540485 464674 336442 572655 724577 627822 553055 986861 944776 588636 966817 892103 737744 478475 668429 809085 362250 597680'
str_c = list(str_c.split(' '))

c = [int(i) for i in str_c]
k = 18





