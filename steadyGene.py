#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:07:17 2019

@author: hankui
"""

#%%
#gene = 'GAAATAAA'
gene = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'


#%%
from collections import Counter

# Number per Class
nc = len(gene)/4 # every letter sgould have this many appearances
tbr = 0
ind_l = [] # indices for the list of letters not to be replaced

for i, val in enumerate(Counter(gene).values()):
    #import pdb; pdb.set_trace()

    tbr += val % 4 # number of letters to be replaced in gene
    
    # find the letters that are not to be replaced
    if val < nc:
        l = list(Counter(gene).keys())[i] # the letter to be fixated
        ind_l.append(gene.index(l))

# calculate the gap lengths in between fixed letters
#ind_l.append(len(gene))
#for i in range(len(ind_l)-1):
#    print(ind_l[i+1] - ind_l[i] - 1)

#%%
# a 0-1 vector indicating whether a gene should be replaced or not
indicator = [1 for v in range(len(gene))]
for i in ind_l:
    indicator[i] = 0        


#%% difference in the indices of those values whose consecutive cumulative sum is tbr
import numpy as np
count = 0 # number of letters that have found a lcation to replace in
CurMin = sum(np.cumsum(indicator) <= tbr)

for i in range(len(gene)-tbr):
    #import pdb; pdb.set_trace()
    # current minimum number of replacements needed
    TmpMin = sum(np.cumsum(indicator[i:]) <= tbr)
    if TmpMin < CurMin:
        CurMin = TmpMin


#%%
from collections import Counter
import numpy as np

def steadyGene(gene):
    import pdb; pdb.set_trace()
    # Number per Class
    nc = len(gene)/4 # every letter sgould have this many appearances
    tbr = 0
    ind_l = [] # indices for the list of letters not to be replaced

    for i, val in enumerate(Counter(gene).values()):
        #import pdb; pdb.set_trace()

        tbr += val % 4 # number of letters to be replaced in gene
    
        # find the letters that are not to be replaced
        if val < nc:
            l = list(Counter(gene).keys())[i] # the letter to be fixated
            ind_l.append(gene.index(l))
    
    # a 0-1 vector indicating whether a gene should be replaced or not
    indicator = [1 for v in range(len(gene))]
    for i in ind_l:
        indicator[i] = 0        

    count = 0 # number of letters that have found a lcation to replace in
    cumsums = []

    for iter in range(len(indicator)):
        cumsums.append(sum(indicator[:iter+1]))
    CurMin = sum([ v <= tbr for v in cumsums])

    for i in range(len(gene)-tbr):
        #import pdb; pdb.set_trace()
        # current minimum number of replacements needed
        cumsums = []

        for iter in range(len(indicator[i:])):
            cumsums.append(sum(indicator[i:i+iter+1]))
        TmpMin = sum([ v <= tbr for v in cumsums])
        #TmpMin = sum(np.cumsum(indicator[i:]) <= tbr)
        if TmpMin < CurMin:
            CurMin = TmpMin
    
    return CurMin







