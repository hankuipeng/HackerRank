#%%
a = [3,1,2]
#%%
numSwaps = 0

while True:
    SwapsFlag = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1
            SwapsFlag = True
    if not SwapsFlag:
        break


print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])


#%%
def countSwaps(a):
    Nswaps = 0
    
    while True:
        flag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                #swap = a[i]
                #a[i+1] = a[i]
                #a[i] = swap
                a[i], a[i+1] = a[i+1], a[i]
                Nswaps += 1
                flag = True
        if not flag:
            break
    
    print('Array is sorted in '+str(Nswaps)+' swaps.')
    print('First element: '+str(a[0]))
    print('Last element: '+str(max(a)))

#%%
######## attempt 1

def countSwaps(a):
    Nswaps = 0
    #swap = 0
    copy = a
    for i in range(len(a)):
        for j in range(len(a)):
            if copy[i] > a[j]:
                swap = copy[i]
                a[j] = copy[i]
                copy[i] = swap
                Nswaps += 1
    print('Array is sorted in '+str(Nswaps)+' swaps.')
    print('First element: '+str(a[0]))
    print('Last element: '+str(a[-1]))


#%% ##### attempt 2
def countSwaps(a):
    Nswaps = 0
    
    while True:
        flag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap = a[i]
                a[i+1] = a[i]
                a[i] = swap
                Nswaps += 1
                flag = True
        if not flag:
            break
    
    print('Array is sorted in '+str(Nswaps)+' swaps.')
    print('First element: '+str(min(a)))
    print('Last element: '+str(max(a)))
