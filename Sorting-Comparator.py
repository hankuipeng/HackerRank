#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr  5 11:44:37 2020

@author: hankui

"""


# Link to the challenge:
# https://www.hackerrank.com/interview/interview-preparation-kit/sorting/challenges


#%% 
from functools import cmp_to_key


#%% the class that I am meant to finish 
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
       
    def comparator(a, b):
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0


#%% testing
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))


#%% print the sorted result 
for i in data:
    print(i.name, i.score)


#%% Misc
sorted("This is a test string from Andrew".split(), key=str.lower)
