#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr  6 21:07:54 2020

@author: hankui

"""


#%% get the array from keyboard input
arr = list(map(int, input().rstrip().split()))


#%% specify the test instance
arr = [2, 1, 3, 1, 2]


#%%
count = 0
for i in range(1,len(arr),2): # start index, end index, step
    
    # step 1: merge into twos
    if arr[i-1] > arr[i]:
        swap = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = swap
        count += 1


#%% solution 1
def merge(arr0, arr1):

    inversions = 0
    result = []

    # two indices to keep track of where we are in the array
    i0 = 0
    i1 = 0

    # probably doesn't really save much time but neater than calling len() everywhere
    len0 = len(arr0)
    len1 = len(arr1)
    
    import pdb
    pdb.set_trace()
    
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions

# testing 
merge(arr, arr)


#%% solution 2
def merge(arr, left_half, right_half):
    i, j, k = 0, 0, 0
    inversions = 0
    left_len, right_len = len(left_half), len(right_half)
    import pdb
    pdb.set_trace()
    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversions += left_len - i
        k += 1

    while i < left_len:
        arr[k] = left_half[i]
        i, k = i+1, k+1

    while j < right_len:
        arr[k] = right_half[j]
        j, k = j+1, k+1

    return inversions

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # this is equivalent to floor(len(arr)/2) in MATLAB
        left_half, right_half = arr[:mid], arr[mid:]
        
        import pdb
        pdb.set_trace()
        inversions = merge_sort(left_half) + merge_sort(right_half) + merge(arr, left_half, right_half)
        return inversions
    return 0

def countInversions(arr):
    return merge_sort(arr)


#%%
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        print(countInversions(arr))



