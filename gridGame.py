#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:43:27 2019

@author: Hankui Peng

"""

#%%
grid = [[0, 0, 0, 0],[1, 0, 0, 1]]
k = 1 # number of steps to play

rules = ['dead','alive','dead','dead','dead','dead','dead','dead','dead','dead']


#%%
def gridGame(grid, k, rules):
    m = len(grid) 
    n = len(grid[0])
    #import pdb; pdb.set_trace()
    Nrules = len(rules)
    ind = rules.index('alive')
    neigh_mat = [[0 for i in range(n)] for j in range(m)]
    
    #Farr = grid
    iterr=0
    while iterr < k:
        # four corners
        neigh_mat[0][0] = grid[0][1]+grid[1][0]+grid[1][1] # upper left
        neigh_mat[0][-1] = grid[0][-2]+grid[1][-1]+grid[1][-2] # upper right 
        neigh_mat[-1][0] = grid[-2][0]+grid[-1][1]+grid[-2][1] # bottom left
        neigh_mat[-1][-1] = grid[-1][-2]+grid[-2][-1]+grid[-2][-2] # bottom right
    
        # four edges
        if m > 2:
            neigh_mat[1:-1][0] = [grid[i-1][0]+grid[i+1][0]+grid[i-1][1]+grid[i][1]+grid[i+1][1] for i in neigh_mat[1:-1][0]]# left edge
            neigh_mat[1:-1][-1] = [grid[i+1][-1]+grid[i-1][-1]+grid[i+1][-2]+grid[i][-2]+grid[i-1][-2] for i in neigh_mat[1:-1][-1]]# right edge
            
            if n > 2:  
                neigh_mat[0][1:-1] = [grid[0][j-1] + grid[0][j+1] + grid[1][j-1] + grid[1][j] + grid[1][j+1] for j in neigh_mat[0][1:-1]]# top edge
                #neigh_mat[-1][1:-1] = [grid[-1][j-1] + grid[-1][j+1] + grid[-2][j-1] + grid[-2][j] + grid[-2][j+1] for j in neigh_mat[-1][1:-1]]# bottom edge
                
                # middle ones 
                if m > 2 and n > 2: 
                    for i in range(1,m-1):
                        neigh_mat[i][1:n-1] = [grid[i-1][j]+grid[i+1][j]+grid[i][j-1]+grid[i][j+1]+grid[i-1][j-1]+grid[i-1][j+1]+grid[i+1][j-1]+grid[i+1][j+1] for i in neigh_mat[i][1:n-1]]
            
        grid = neigh_mat
        iterr= iterr + 1
                        ##
                        
    return neigh_mat


#%%
gridGame(grid,k,rules)


#%%

for row in grid[0][1:-1]:
    grid[0][row] = 2
    print(row)
    
    
    
    
    
    
    
    