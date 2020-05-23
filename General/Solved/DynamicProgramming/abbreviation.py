#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri May  8 09:45:05 2020

@author: hankui

"""

# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#%% attempt 1
def abbreviation1(a, b):
    
    ans = 'NO'
    counter = 0
    check = []
    #import pdb
    #pdb.set_trace()
    for v in b:
        for i in range(counter, len(a)):
            if a[i] == v.lower():
                counter = i+1
                check.append(1)
                break
    if sum(check) == len(b):
        ans = 'YES'
    return ans 


#%% attempt 2
def abbreviation2(a, b):
    
    ans = 'NO'
    counter = 0
    
    for v in a:
        # when the letter in a is uppercase -- it has to be matched in b
        if v.isupper():
            found = 0
            for i in range(counter, len(b)):
                if v == b[i].upper():
                    found = 1
                    break
            if found == 0:
                break
        #else
    return ans 


#%% attempt 3
def abbreviation3(a, b):
    
    ans = 'NO'
    counter = 0
    check = [0]*len(a)
    
    for v in b:
        for i in range(counter, len(a)):
            if a[i] == v or a[i] == v.lower():
                counter = i+1
                check[i] = 1
                break
    #import pdb
    #pdb.set_trace()
    if sum(check) == len(b):
        logi = [a[ind].isupper() for ind, val in enumerate(check) if val < 1]
        if sum(logi) == 0:
            ans = 'YES'
    return ans 


#%% attempt 4
def abbreviation4(a, b):
    
    ans = 'NO'
    n = len(a)
    m = len(b)
    
    table = [[False]*(n+1) for _ in range(m+1)]
    table[0][0] = True
    
    for j in range(1,n+1):
        if a[j-1].islower():
            table[0][j] = True and table[0][j-1]
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if b[i-1] == a[j-1]:
                table[i][j] = True and table[i-1][j-1]
            elif b[i-1] == a[j-1].upper():
                table[i][j] = table[i][j-1] or table[i-1][j-1]
            elif a[j-1].islower():
                table[i][j] = table[i][j-1]
    
    if table[m][n] == True:
        ans = 'YES'
    return table, ans



#%% one DP solution
def abbreviation(a, b):
    
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(n+1):
        for j in range(1,m+1):
            
            import pdb
            pdb.set_trace()
            
            if a[j-1] == b[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif a[j-1].upper() == b[i-1]:
                dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
            elif a[j-1].islower():
                dp[i][j] = dp[i][j-1]   
    
    return "YES" if dp[n][m] else "NO"


#%%
abbreviation4(a,b)


#%%
a = 'abBGgB'
b = 'BGB'


#%%
a = 'abCdE'
b = 'AFE'


#%% test case 1
a = 'daBcd'
b = 'ABC' # the string to be matched to 


#%% test case 2
a = 'KXzQ'
b = 'K'


#%%
a = 'MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp'
b = 'MBQEVZP'


#%%
a = 'SVAHHHMVIIDYIcOSHMDUAVJRIBxBZQSUBIVEBHfVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAeFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHhMKRDSOQTJYYLTCTSIXIDAnPIHNXENWFFZFJASRZRDAPVYPAViVBLVGRHObnwlcyprcfhdpfjkyvgyzpovsgvlqbhtwrucvszaqinbgeafuswkjrcexvyzq'
b = 'SVAHHHMVIIDYIOSHMDUAVJRIBBZQSUBIVEBHVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHMKRDSOQTJYYLTCTSIXIDAPIHNXENWFFZFJASRZRDAPVYPAVVBLVGRHO'


