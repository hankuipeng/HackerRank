#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:00:09 2019

@author: hankui
"""

import sys 

n = int(input())

# use the dictionary data type
phone_book = dict()

# then read n lines of standard input 
for i in range(n):
    entry = input().split(' ')
    phone_book[entry[0]] = entry[1]

# while there is a valid query to execute
while True:
    try:
        # read in the queries
        query = input()
        #num = phone_book.get(query)
        if query in phone_book:
            print(query+'='+phone_book[query])
        else:
            print('Not found')
    except:
        break

        
#%%
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break