'''
@description: 解析网页测试程序  (中文乱码问题，解码待解决)
@Author: Jkonel
@Date: 2020-06-18 09:54:24
@LastEditors: jkonel
@LastEditTime: 2020-06-19 18:41:31
@param : null
@return: null
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


dat = []
for i in range(1,rang):
    indexs = 0
    name = 'page_1_{0}.html'.format(i)
    path_name = './demo'    #文件夹名字demo,解析python网页
    html = etree.parse(path_name + './' + name, parser = etree.HTMLParser(encoding = 'utf-8'))
    
    items = html.xpath('//div[@class = "dw_table"]/div[@class = "el"]')
    #print(items)
    #-------------------文件解析------------------#
    for item in items:
        dic = {}
        
        salery = item.xpath('.//span[@class = "t4"]/text()')
        if salery:
            salery = salery[0]  #my_rep.get_nums(salery[0])
        else:
            salery = None
        dic['salery'] = salery
        dat.append(dic)

#---------------文件保存----------------#
my_rep.csv_save(dat,'save_test.csv')

