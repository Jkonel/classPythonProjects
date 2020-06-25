'''
@Description: 网页爬取，提取全测试Demo
@Author: Jkonel
@Date: 2020-06-22 17:23:11
@LastEditors: jkonel
@LastEditTime: 2020-06-23 16:24:33
'''
import requests
from lxml import etree
import pandas as pd
import re
from datetime import datetime
import time
import os
import my_reptile


import city_areas_add
import  provence_add
import delet_null
import salary_normalize


my_rep = my_reptile.my_reptile()

###-----------------------------------python爬取网页--------------------------------------###
# python java c/c++ go php   linux 嵌入式软件 嵌入式硬件
'''
rang = 688+1
for i in range(1,rang):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25B5%258C%25E5%2585%25A5%25E5%25BC%258F%25E7%25A1%25AC%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{0}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
    name = 'page_8_{0}.html'.format(i)
    my_rep.page_download(url, name)
'''
###---------------------------------python网页数据提取-----------------------------------###
#folder = './date_2020-6-19/php/'  #网页文件夹
#file_name = 'php.csv'
#my_rep.web_parsing(folder,files_list,file_name)


###--------------------------文件处理-----------------------------------###

folder = './date_2020-6-23/'
files_list = my_rep.get_files_name('./date_2020-6-23/')
print(files_list)

for i in files_list:
    sal_norm = i.split('.')[0] + '_salary_norm.' + i.split('.')[1]
    prov_add = sal_norm.split('.')[0] + '_add_provence.' + sal_norm.split('.')[1]
    city_add = prov_add.split('.')[0] + '_city_area.' + prov_add.split('.')[1]
    del_none = city_add.split('.')[0] + '_del_none.' + city_add.split('.')[1]

    salary_normalize.sal(folder+i, sal_norm)
    provence_add.provence_add(sal_norm, prov_add)
    city_areas_add.divide_city(prov_add, city_add)
    delet_null.delete_null(city_add,del_none)


