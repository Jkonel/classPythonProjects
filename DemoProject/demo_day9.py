'''
@Description: day9 demo py file
@Author: Jkonel
@Date: 2020-06-22 09:39:16
@LastEditors: jkonel
@LastEditTime: 2020-06-22 10:59:57
'''
import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame01 = pd.DataFrame(data, columns=['year', 'state', 'pop'],
                      index=['one', 'two', 'three', 'four','five', 'six'])

## Show date from data base:
print(frame01)
#rows:
print(frame01[1:2]) #rows

print(frame01.head(2))
print(frame01[:2])

print(frame01.tail(2))
print(frame01[-2:])
#columns:
print(frame01['state']) #one column
print(frame01[['state','year']])    #some columns
print(frame01.loc['one','state'])   #name finding
print(frame01.iloc[1,2])    #index finding 

## Aggregate function
pops = frame01['pop']
print(type(pops))

print(pops.sum())   #sum all in a colum
print(pops.mean())  #mean all in a column
print(pops.count()) #count all in all colums
print(frame01.info())   #show data frame information
print(pops.shape)   #shape of a column
print(pops.ndim)

## delete data
new_frame01 = frame01.drop(['state'],axis = 1)  #pop out columns that user pointed.
new_frame02 = frame01.drop(['one'],axis=0)  #pop out rows that user pointed.
new_frame022 = new_frame02.drop(['state'],axis=1,inplace=True)  #pop out data from the original date base.
new_frame03 = frame01.drop(frame01.index[1:2],axis=0)  #pop out rows according to the indexs be giving.
new_frame04 = frame01.drop(frame01.columns[1:2],axis=1)  #pop out columns according to the indexs be giving.
print(new_frame01)
print(new_frame02)
print(new_frame03)
print(frame01)  #the original data remains unchanged.

## NAN processing
frame01.dropna(axis = 0)    #delete nan in rows.
frame01.dropna(axis = 1)    #delete nan in columns.
frame01.dropna(subset=['state'],axis = 1)   #point the subset.

frame01.fillna(method = 'ffill')
frame01.fillna(method = 'bfill')
# pad/ffill：用前一个非缺失值去填充该缺失值
# backfill/bfill：用下一个非缺失值填充该缺失值
# None：指定一个值去替换缺失值（缺省默认这种方式）

frame01['state'].fillna(frame01['state'].mean(),inplace = True) #using mean fufill nan




