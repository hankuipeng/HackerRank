#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 17 09:25:37 2020

@author: Hankui Peng

"""


# Link to question: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

### Relevant Python knowledge used 

## 1. Convert letter to integer

# approach 1
import string
(string.ascii_lowercase.index('c') + 3)

# approach 2
chr(ord('a') + 3)

## 2. check if a string is in the alphabet
str.isalpha('a')


## Inputs
s = 'middle-Outz'
k = 2

s = '159357lcfd'
k = 98

output = []

for letter in s:
    
    if str.isalpha(letter):
        
        if str.islower(letter):
            
            remainder = (ord(letter) - 96 + k)%26
            if remainder == 0:
                remainder = 26
                
            output.append(chr(remainder + 96))  
        else:
            letter_new = str.lower(letter)
            
            remainder = (ord(letter_new) - 96 + k)%26
            if remainder == 0:
                remainder = 26
            
            output.append(str.upper(chr(remainder + 96)))
    else:
        
        output.append(letter)

''.join(output)