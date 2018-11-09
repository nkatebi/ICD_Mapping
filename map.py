#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:17:48 2018

@author: nkatebi
This code is for finding the number of one to one, one to many mappings and no map.
For this purpose flags of the mapping are used. Approximate flag is the first one
which shows there is an approximate match or identical match. Next flag is No map 
which is for indicating that there is any map or not and the third one is combination
flag for checking that the code maps to more than one code or not.
"""
################ loading mapping files #################

import sys
        
        
 ############# this function is for counting the number of mappings ############       
def map_icd(path):
    '''
    Input: path of mapping text file
    output: number of one to one one to many and no map
        
    '''
    with open(path,'r') as text:
        flag=[]
        for line in text:
            A=line.split()
            flag.append(A[2])
    # no map and combination flags are zero
    one_one=0
    for i in range(len(flag)):
        if int(flag[i][1])==0 and int(flag[i][2])==0:
            one_one=one_one+1
            
    # no map is zero and combination is one        
    one_many=0
    for i in range(len(flag)):
        if int(flag[i][1])==0 and int(flag[i][2])==1:
            one_many=one_many+1
            # no map flag is one
    no_map=0
    for i in range(len(flag)):
       if int(flag[i][1])==1:
           no_map=no_map+1

    return one_one,one_many,no_map




if __name__== "__main__":
    [one_one9to10,one_many9to10,no_map9to10]=map_icd(sys.argv[1])
    print('Number of one to one mappings in ICD 9 to 10 ',one_one9to10)
    print('Number of one to many mappings in ICD 9 to 10 ',one_many9to10)
    print('Number of no maps in ICD 9 to10 ',no_map9to10)

    [one_one10to9,one_many10to9,no_map10to9]=map_icd(sys.argv[2])
    print('Number of one to one mappings in ICD 10 to 9 ',one_one10to9)
    print('Number of one to many mappings in ICD 10 to 9 ',one_many10to9)
    print('Number of no maps in ICD 10 to 9 ',no_map10to9)
