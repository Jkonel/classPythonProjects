'''
@Description: main.py
@Author: Jkonel
@Date: 2020-06-18 09:54:24
@LastEditors: jkonel
@LastEditTime: 2020-06-19 18:49:07
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

rang = 688+1

# python java c/c++ go php   linux 嵌入式软件 嵌入式硬件

for i in range(1,rang):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25B5%258C%25E5%2585%25A5%25E5%25BC%258F%25E7%25A1%25AC%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{0}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
    name = 'page_8_{0}.html'.format(i)
    my_rep.page_download(url, name)
    

# 子页面读取
indexs = 0

for i in range(1,rang):
    indexs = 0
    name = 'page_1_{0}.html'.format(i)
    path_name = './demo'
    html = etree.parse(path_name + './' + name, parser = etree.HTMLParser(encoding = 'utf-8'))
    
    items = html.xpath('//div[@class = "dw_table"]/div[@class = "el"]')
    #print(items)
    #-------------------文件解析------------------#
    for item in items:
        inside = item.xpath('.//div[@class = "s_l_name"]/a/@href')
        name2 = 'page_2_{0}_{1}.html'.format(i,indexs)
        #time.sleep(3)
        my_rep.page_download(inside,name2)
        indexs += 1

#---------------文件保存----------------#
#my_rep.csv_save(dat,'save_test.csv')

