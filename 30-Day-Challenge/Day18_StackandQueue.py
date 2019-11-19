#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:25:04 2019

@author: hankui
"""


#%%
import sys
from collections import deque


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = deque()

    def pushCharacter(self, character): # a 'stack' reaches from the end 
        self.stack.append(character)
    
    def enqueueCharacter(self, character): # a 'queue' reaches from the front
        self.queue.append(character)

    def popCharacter(self):
        self.stack.pop()
    
    def dequeueCharacter(self):
        self.queue.popleft()

#%% solution
  class Solution:
      def __init__(self):
          self.mystack = list()
          self.myqueue = list()
          return(None)

      def pushCharacter(self, char):
          self.mystack.append(char)

      def popCharacter(self):
          return(self.mystack.pop(-1))

      def enqueueCharacter(self, char):
          self.myqueue.append(char)

      def dequeueCharacter(self):
          return(self.myqueue.pop(0))


#%%
# read the string s
#s=input()
s = 'yes'
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
#%%
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    