#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:15:45 2019

@author: hankui
"""

#%%
tring1 = input()
string2 = input()
 
def string_out(string):
    if len(string) <= 8:
        print(string+"0"*(8-len(string)))
    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
        print(string+"0"*(8-len(string)))
    return
 
string_out(string1)
string_out(string2)