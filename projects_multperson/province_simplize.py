'''
@Description: 修补函数，将csv数据中的省名字进行简化处理
@Author: Jkonel
@Date: 2020-06-24 19:54:40
@LastEditors: jkonel
@LastEditTime: 2020-06-24 20:33:34
'''

import city2provence
import os
import my_reptile
import pandas as pd


my_rep = my_reptile.my_reptile()

folder = './filted_data'    #网页文件夹
files_list = my_rep.get_files_name(folder)

for i in files_list:
    prov = []
    smax = []
    smin = []
    frame = pd.read_csv(folder+'/'+ i)
    #print(frame)
    frame = frame.drop('province', axis=1)
    addr = frame['address']

    frame['salary_max'] = pd.to_numeric(frame['salary_max'], errors='coerce')
    frame['salary_min'] = pd.to_numeric(frame['salary_min'], errors='coerce')

    for j in addr:
        prov.append(city2provence.city2provence(city2provence.city_get(j)))
    frame['province'] = prov
    my_rep.csv_save(frame, i)

