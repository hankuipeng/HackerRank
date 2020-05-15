#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:51:19 2019

@author: hankui
"""


#%%
queries = [(3, 4),
(2, 1003),
(1, 16),
(3, 1)]


#%%
import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
from collections import Counter
def freqQuery(queries):
    n = len(queries)
    ans = []
    seqCt = Counter() # counter for the sequence 
    
    for qi in queries:
        #print(qi)
        if qi[0] == 1:
            seqCt[qi[1]] += 1
        elif qi[0] == 2:
            seqCt[qi[1]] -= 1
        else:
            freqs = [seqCt[i] for i in seqCt] # get all frequencies
            if qi[1] in freqs:
                ans.append(1)
            else:
                ans.append(0)
    return ans


#%% submission
from collections import Counter
def freqQuery(queries):
    
    n = len(queries)
    
    freq = Counter()
    cnt = Counter()

    arr = []
    
    import pdb
    pdb.set_trace()
    
    for q in queries:
        
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr


#%%
queries = [
[3, 4],
[2, 1003],
[1, 16],
[3, 1]]

freqQuery(queries)


#%%
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
