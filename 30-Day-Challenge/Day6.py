#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:25:13 2019

@author: hankui
"""

#%%
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_test_cases = int(input())

for i in range(num_test_cases):
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''

    for j in range(len(test_string)):
        if j % 2:
            odd_indexed_characters += test_string[j]
        else:
            even_indexed_characters += test_string[j]
    print(even_indexed_characters+' '+odd_indexed_characters)
