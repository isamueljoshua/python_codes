# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:34:56 2017

@author: Administrator
"""

import pandas
df = pandas.read_excel('Exceltest.xlsx')
#print the column names
print df.columns
#get the values for a given column
values = df['INDEX'].values
#print values
#get a data frame with selected columns
FORMAT = ['INDEX', 'C1', 'C2']
df_selected = df[FORMAT]
print df_selected