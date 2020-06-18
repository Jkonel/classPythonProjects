'''
@Description: main.py
@Author: Jkonel
@Date: 2020-06-18 09:54:24
@LastEditors: jkonel
@LastEditTime: 2020-06-18 17:46:34
'''

import requests
from lxml import etree
import pandas as pd
import re
from datetime import datetime
import time
import os

import my_reptile


my_rep = my_reptile.my_reptile()

rang = 95+1

for i in range(1,rang):
    url = 'http://search.jumei.com/?filter=0-11-{0}&search=%E5%8F%A3%E7%BA%A2&from=search_toplist_%E5%8F%A3%E7%BA%A2_word_pos_6&cat='.format(i)
    name = 'page_1_{0}.html'.format(i)
    my_rep.page_download(url, name)
    


# 子页面读取

indexs = 0

for i in range(1,rang):
    indexs = 0
    name = 'page_1_{0}.html'.format(i)
    path_name = './date_{0}'.format(my_rep.text_time()[1])
    html = etree.parse(path_name+'/'+name, parser = etree.HTMLParser(encoding = 'utf-8'))
    
    items = html.xpath('//div[@class = "products_wrap"]/ul/li')
    #-------------------文件解析------------------#
    for item in items:
        inside = item.xpath('.//div[@class = "s_l_name"]/a/@href')
        if inside:
            inside = inside[0]
        else:
            inside = None
        print(inside)

        name2 = 'page_2_{0}_{1}.html'.format(i,indexs)
        #time.sleep(3)
        my_rep.page_download(inside,name2)
        indexs += 1

#---------------文件保存----------------#
#df = pd.DataFrame(data)
#df.to_csv('./htmls/data.csv',index = 0,na_rep = 'NA')
