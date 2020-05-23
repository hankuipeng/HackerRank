#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue May 19 22:25:06 2020

@author: hankui

"""


#%%
def maxCircle(queries):
    # contains a dictionary of dictionaries 
    # with each dictionary within it being a friend group
    metaCircle = []
    
    for i, pair in enumerate(queries):
        
        # search for the locations of the values in 'pairs' in metaCircle
        loc0 = []
        loc1 = []
        for ind, val in enumerate(metaCircle):
            if pair[0] in val:
                loc0 = ind
            if pair[1] in val:
                loc1 = ind
        
        # if only loc0 already exists
        if type(loc0) == int and type(loc1) != int: 
            metaCircle[loc0].append(pair[1])
        
        # if only loc1 already exists
        elif type(loc0) != int and type(loc1) == int:
            metaCircle[loc1].append(loc0)
        
        # if both of them exists
        elif type(loc0) == int and type(loc1) == int:
            #import pdb
            #pdb.set_trace()
            metaCircle[loc0].extend(metaCircle[loc1])
            metaCircle[loc0] = list(set(metaCircle[loc0]))
            metaCircle[loc1] = []
        
        # if none of them exists
        else:
            metaCircle.append(pair)
    
        num = max([len(v) for v in metaCircle])
        print(num)


#%%
queries = [[1, 2],[3, 4],[1, 3],[5, 7],[5, 6],[7, 4]]

maxCircle(queries)
