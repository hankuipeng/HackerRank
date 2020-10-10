#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 10 08:59:39 2020

@author: Hankui Peng

"""

# Link to question: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

test1 = 'hhaacckkekraraannk'

test2 = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'

oracle = 'hackerrank'

count_dict = {}


for i,v in enumerate(test1):
        
        count_dict[v].append(i)


# one solution
# '.' symbol matches any single character  
# '*' symbol matches zero or more occurrences of the symbol left to it 
import re

# one expression
print( (re.search('.*'.join("hackerrank"), test1) and "YES") or "NO")

# alternative expression
result = re.search('.*'.join("hackerrank"), test1)

if result:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)