#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Tue Apr 14 10:14:58 2020

@author: hankui

"""


#%%
import collections

def isValid(s):

    ans = 'NO'
    
    ctr = collections.Counter(s)
    
    # create a list of the frequencies of all letters
    li = []
    for val in ctr:
        li.append(ctr[val])
    ctr_num = collections.Counter(li)
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    if len(ctr_num) == 1:
        ans = 'YES'
    if len(ctr_num) == 2:
        
        vals = [v for v in ctr_num]
        freqs = [ctr_num[vals[0]],ctr_num[vals[1]]]
        
        if min(freqs) == 1 and abs(vals[0]-vals[1]) == 1:
            ans = 'YES'
        
        if  min(vals) == 1 and ctr_num[1] == 1:
            ans = 'YES'
    return ans


#%%
#s = 'abc'
#s = 'abcdefghhgfedecba'
#s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
s = 'aaaaabc'
#s = 'abcdefghhgfedecba'

#%%
isValid(s)


