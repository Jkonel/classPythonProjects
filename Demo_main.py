'''
@Description: 网页爬取，提取全测试Demo
@Author: Jkonel
@Date: 2020-06-22 17:23:11
@LastEditors: jkonel
@LastEditTime: 2020-06-22 17:25:54
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

folder = '../date_2020-6-19'    #网页文件夹
files_list = my_rep.get_files_name(folder)

my_rep.web_parsing(folder,files_list,'page_1.csv')


