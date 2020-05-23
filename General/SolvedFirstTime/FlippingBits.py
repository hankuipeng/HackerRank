#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:59:25 2020

@author: hankui
"""


#%%

# reference for converting a number to base 2:
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base#2267428
bi = "{0:b}".format(0) 

n0 = 32-len(bi)
original = '0'*n0+bi
opposite = ''
for ind, val in enumerate(original):
    if val=='0':
        opposite += '1'
    if val=='1':
        opposite += '0'

num = 0
for i in range(len(opposite)):
    num += (2**i)*int(opposite[-(i+1)])