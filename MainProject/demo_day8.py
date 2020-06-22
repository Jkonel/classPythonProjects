'''
@Description: pandas test
@Author: Jkonel
@Date: 2020-06-19 14:49:19
@LastEditors: jkonel
@LastEditTime: 2020-06-19 16:47:08
'''
import pandas as pd
import numpy as np

#jobs = pd.read_csv('./job51_java.csv')
#jobs = pd.read_csv('./DemoProject/job51_java.csv')

ser01 = pd.Series(list('all is shit'))

dat = pd.DataFrame(np.arange(100).reshape(10,10),index = [str(i) for i in range(10)],columns=[ str(i) for i in range(1,11)])

print(dat.iloc[2,3])

#print(jobs.index)
print(dat)
