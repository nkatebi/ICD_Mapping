#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:31:16 2018

@author: nkatebi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:32:07 2018
@author: nkatebi
"""
import sys
import pandas as pd
def reducemapping(path1,path2,path3):# 1-many mappings
    df = pd.read_fwf(path1, sep=' ', header=None,names= ['icd10','icd9','flags'],converters= {0: str, 1:str, 2:str})
    grouped=df.groupby('icd10')
    one_to_many=grouped.filter(lambda x: len(x) > 1)
    
    ############ loading ICD 10 and ICD 9 codes and ICD 9 code frequency
    df = pd.read_csv(path2, sep='\t', header=None)
    code10=df[df.columns[0]]
    new = code10.str.split(".", n = 1, expand = True)
    ICD10code = new[0].astype(str).str.cat(new[1].astype(str))
    df = pd.read_csv(path3, sep='\t', header=None)
    code9=df[df.columns[0]]
    new = code9.str.split(".", n = 1, expand = True)
    ICD9code = new[0].astype(str).str.cat(new[1].astype(str))
    TotalDiag=df[df.columns[1]]
    
    #####################################################
    
    text_file = open("Output.txt", "w")
     
    I10=one_to_many[one_to_many.columns[0]]  
    I9=one_to_many[one_to_many.columns[1]]       
    for row in ICD10code:
        oneone9=''
        temp=I10[I10.str.match(row)]
        if temp.any():
            a=temp.index
            freq=0
            for i in range(len(a)):
                relatedicd9=I9.loc[a[i]]
                temp2=ICD9code[ICD9code.str.match(relatedicd9)]
                if temp2.any():
                    b=temp2.index
                    newfreq=TotalDiag.loc[b[0]]
                    if int(newfreq)>int(freq):
                        freq=newfreq
                        oneone9=temp2.loc[b[0]]
        if oneone9 != '':
            text_file.write(str(row)+'\t'+str(oneone9)+'\t'+str(freq)+'\n')
            print('ICD9 is '+oneone9)
            print('ICD10 is '+row)
    text_file.close()
if __name__== "__main__":
    reducemapping(sys.argv[1],sys.argv[2],sys.argv[3])
                    

