#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:39:10 2019

@author: Hankui Peng

"""

#%%

primes =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    answer = 0
    Z = 1
    if n > 5:
        while Z<=n:
            Z = Z*primes[answer]
            answer = answer + 1
        answer = answer-1
    elif n>1:
        answer = 1
    else:
        answer = 0
    
    return answer


def baobeiprimes(n):
    
    primes = [2,3,5,7,11,13,17,19,23,29,21,37,39,41,43,47,53]
    
    
    prod = 2
    count = 0
    
    #if n==1:
    #    return count
    if n>1:
        while prod <= n:
            prod = prod*primes[count+1]
            count += 1
    
    return count   

#%%
def primeCount(n):
    #factors = 0
    count = 0
    primes = 2 # the first prime number 
    prod = 2
        
    if n > 1:
        
        #factors = 1
        
        while prod <= n: # check if val_cand is a prime number 
            #import pdb; pdb.set_trace()
            count += 1
            
            # find the next prime number 
            foundNext = 0 # find the next prime
            cand = primes+1
            while foundNext < 1:
                logic_ind = [cand%val==0 for val in range(1,cand+1)]
                if logic_ind[0]+logic_ind[-1] == 2 and sum(logic_ind[1:-1])==0:
                
                    foundNext = 1
                    primes = cand
                else:
                    cand += 1
            
            prod = prod*primes
            
            
    return count


#%%
# find the next prime number 
            #for cand in range(primes+1,n+1):
             #try:  
foundNext = 0 # find the next prime
cand = primes+1
while foundNext < 1:
    import pdb; pdb.set_trace()
    for i in range(2,cand):
        if (cand % i) == 0:
            break
        else:
            #foundNext = 1
            #primes = cand
            break
    cand += 1
#%%
foundNext = 0 # find the next prime
cand = primes+1
while foundNext < 1:
    logic_ind = [cand%val==0 for val in range(1,cand+1)]
    if logic_ind[0]+logic_ind[-1] == 2 and sum(logic_ind[1:-1])==0:
        
        foundNext = 1
        primes = cand
    else:
        cand += 1