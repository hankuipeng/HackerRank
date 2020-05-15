#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May 13 12:31:28 2020

@author: hankui
"""

#%%
tbf = [
'+-++++++++',
'+-++++++++',
'+-++++++++',
'+-----++++',
'+-+++-++++',
'+-+++-++++',
'+++++-++++',
'++------++',
'+++++-++++',
'+++++-++++',]

words = ['LONDON','DELHI','ICELAND','ANKARA']


#%%
# 1. find a minus sign
# 2. determine whether the word is in row or column
for i in range(len(tbf)):
    for j in range(10):
        
        if tbf[i][j] == '-': # if we found a word
            import pdb
            pdb.set_trace()
            # determine the direction of the word: in column
            if tbf[i+1][j] == '-' and tbf[i][j+1] == '+':
                loc = [tbf[i][j]]
                l = 1
                while l < 10:
                    if tbf[i+l][j] == '-':
                        loc.append(tbf[i+l][j])
                        l += 1
                    else:
                        break


#%% one solution 
def printBoard(board):
    for row in board:
        print(''.join(row))
    
def possibleDirections(board,word):
    length=len(word)
    
    for i in range(10):
        for j in range(10):
            
            properSlotH = True
            properSlotV = True

            for k in range(length):
                #Horizontal direction, axis marked as 0:
                if j<10-length+1:
                    if board[i][j+k] not in ['-',word[k]]:
                        properSlotH = False
                        
                #Vertival direction, axis marked as 1:        
                if i<10-length+1: 
                    if board[i+k][j] not in ['-',word[k]]:
                        properSlotV = False

            if properSlotH and j<10-length+1:
                yield (i,j,0)
            if properSlotV and i<10-length+1:
                yield (i,j,1)    
            
def move(board,word,startLocation):
    i,j,axis=startLocation
    length=len(word)
    if axis == 0:
        for k in range(length):
            board[i][j+k]=word[k]
    else:
        for k in range(length):
            board[i+k][j]=word[k]
            
def rollback(board,word,startLocation):
    i,j,axis=startLocation
    length=len(word)
    if axis == 0:
        for k in range(length):
            board[i][j+k]='-'
    else:
        for k in range(length):
            board[i+k][j]='-'
        
def crosswordPuzzle(board,words):
    global solved
    if len(words) == 0:
        if not solved:
            printBoard(board)
        solved=True
        return 
    
    word=words.pop()
    
    for direction in possibleDirections(board,word):
        move(board,word,direction)
        solve(board,words)
        rollback(board,word,direction)
    
    words.append(word)

if __name__ == '__main__':
    board = []
    for _ in range(10):
        board_item = list(input())
        board.append(board_item)

    words = str(input()).split(";")
    solved=False
    
    solve(board,words)
