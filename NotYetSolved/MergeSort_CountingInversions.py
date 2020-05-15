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


#%% attempt 2020/05/13
def merge_sort(arr):
    count = 0
    # The last array split
    if len(arr) <= 1:
        return arr, count
    mid = len(arr) // 2
    
    # Perform merge_sort recursively on both halves
    left, countl = merge_sort(arr[:mid])
    right, countr = merge_sort(arr[mid:])
    
    count = countl + countr
    
    merged, count = merge(left, right, arr.copy(), count)
    
    return merged, count

def merge(left, right, merged, count):
    
    left_cursor, right_cursor = 0, 0
    
    
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            count += len(left)-left_cursor
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged, count 


#%% attempt 2020/05/12
def countInversions(arr):

    count = 0 # current count of the number of swaps
    sublists = []
    
    ## step 1: compare every pair that exists in the array
    count, arr, sublists = CompareWithin(count, arr)
    
    ## step 2: compare the border cases for pairs of sublists
    for ind, sublist in enumerate(sublists[:len(sublists)-1]):
        #import pdb
        #pdb.set_trace()
        
        list_pair = [sublist, sublists[ind+1]]
        
        # we need to compare the pair and update the count 
        count, pair = Compare(count, list_pair)
    
    arr = [y for x in sublists for y in x] # flatten the list of lists
    
    count, arr, sublists = CompareWithin(count, arr)
    for ind, sublist in enumerate(sublists[:len(sublists)-1]):
        #import pdb
        #pdb.set_trace()
        
        list_pair = [sublist, sublists[ind+1]]
        
        # we need to compare the pair and update the count 
        count, pair = Compare(count, list_pair)
    
    return count 

def Compare(count, lists):
    list1 = lists[0]
    list2 = lists[1]
    if list1[-1] > list2[0]:
        count += 1
        list1[-1], list2[0] = list2[0], list1[-1]
    lists = [list1,list2]
    return count, lists

def CompareWithin(count, arr):
    ### Inputs:
    # current count number
    # current state of the array 
    
    i = 0
    sublists = []
    
    while i < len(arr):
        
        if i == len(arr)-1 and len(arr)%2 == 1:
            sublists.append([arr[i]])
            pass
        else:
            
            pair = [arr[i], arr[i+1]]
            
            if min(pair) != arr[i]:
                count += 1
                arr[i] , arr[i+1] = min(pair), max(pair)
                
            sublists.append([arr[i], arr[i+1]]) # current pair after comparison 
        
        i += 2
    return count, arr, sublists


#%% one solution
def sort_pair(arr0, arr1):
    if len(arr0) > len(arr1):
        return arr1, arr0
    else:
        return arr0, arr1
    
def merge(arr0, arr1):
    
    inversions = 0
    result = []
    
    # two indices to keep track of where we are in the array
    i0 = 0
    i1 = 0
    
    # probably doesn't really save much time but neater than calling len() everywhere
    len0 = len(arr0)
    len1 = len(arr1)
    
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len(arr0[i0:])
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions

def sort(arr):
    length = len(arr)
    mid = length//2
    if length >= 2:
        sorted_0, counts_0 = sort(arr[:mid])
        sorted_1, counts_1 = sort(arr[mid:])
        result, counts = merge(sorted_0, sorted_1)
        return result, counts + counts_0 + counts_1
    else:
        return arr, 0

def countInversions(a):
    final_array, inversions = sort(a)
    # print(final_array)
    return inversions
     

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



