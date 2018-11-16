#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:32:07 2018

@author: nkatebi
"""
import pandas as pd
# 1-many mappings
df = pd.read_fwf('./2018_I10gem.txt', sep=' ', header=None,names= ['icd10','icd9','flags'],converters= {0: str, 1:str, 2:str})
grouped=df.groupby('icd10')
one_to_many=grouped.filter(lambda x: len(x) > 1)

############ loading ICD 10 and ICD 9 codes and ICD 9 code frequency
df = pd.read_csv('./ICD10CM.txt', sep='\t', header=None)
code10=df[df.columns[0]]
new = code10.str.split(".", n = 1, expand = True)
ICD10code = new[0].astype(str).str.cat(new[1].astype(str))
df = pd.read_csv('./ICD9CM.txt', sep='\t', header=None)
code9=df[df.columns[0]]
new = code9.str.split(".", n = 1, expand = True)
ICD9code = new[0].astype(str).str.cat(new[1].astype(str))
TotalDiag=df[df.columns[1]]

#####################################################
#unique10=ICD10code.unique()
#temp=one_to_many[one_to_many.columns[0]].isin(ICD10code)
#for index,row in temp:
#    if row=='True':
#  
I10=one_to_many[one_to_many.columns[0]]  
I9=one_to_many[one_to_many.columns[1]]       
for row in ICD10code[1:50]:
    temp=I10[I10.str.match(row)]
    if temp.any():
        a=temp.index
        for i in range(len(a)):
        
            relatedicd9=I9.loc[a[i]]
            for n in relatedicd9:
                temp2=ICD9code[ICD9code.str.match(n)]
                b=temp2.index
                freq=0
                for j in range(len(b)):
                    newfreq=TotalDiag.loc[b[j]]
                    if int(newfreq)>int(freq):
                        freq=newfreq
                        oneone9=temp2.loc[b[j]]
                print('ICD9 is '+oneone9)
                print('ICD10 is '+row)
                    

            




