# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

c = [0,1,0,0,0,1,0]
#%%
def jumpingOnClouds(c):
    n = len(c)
    Njump = 0
    counter = 0
    while counter < (n-2):
        if c[counter+2] == 0:
            Njump = Njump + 1
            counter = counter + 2
        else:
            Njump = Njump + 1
            counter = counter + 1
        print(counter)
    if counter < (n-1):
        Njump = Njump + 1
    return Njump