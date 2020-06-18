'''
@Description: main.py
@Author: Jkonel
@Date: 2020-06-18 09:54:24
@LastEditors: jkonel
@LastEditTime: 2020-06-18 10:58:04
'''

import requests
from lxml import etree
import pandas as pd
import re
from datetime import datetime
import time
import os


class my_reptile:
    def __init__(self):
        pass
    def text_time(self):
        tim = time.time()
        res = datetime.fromtimestamp(tim) 
        strc_exact = '{0}-{1}-{2}-{3}_{4}_{5}_{6}'.format(res.year, res.month, res.day, res.hour, res.minute, res.second, res.microsecond)
        strc_day = '{0}-{1}-{2}'.format(res.year, res.month, res.day)
        strc_min = '{0}-{1}-{2}-{3}_{4}'.format(res.year, res.month, res.day, res.hour, res.minute)
        return [strc_exact,strc_day,strc_min]

    def page_download(self, url, name):
        headers = {'user-agent': 'Mozilla/5.0'}
        path_name = './date_{0}'.format(self.text_time()[1])
        log_name = '{0}/log_{1}.txt'.format(path_name,self.text_time()[2])

        if not os.path.isdir(path_name):
            os.mkdir(path_name)
        if not os.path.isfile(log_name):
            with open(log_name,'w') as pp:
                pp.write('{0}/日志记录:{1}:\n'.format(path_name,self.text_time()[0]))

        respond = requests.get(url,headers = headers)
        if respond.status_code == 200:
            with open('{0}/{1}'.format(path_name,name),'w',encoding='utf-8') as fp:
                fp.write(respond.text)
            with open(log_name,'a') as pp:
                pp.write(self.text_time()[0] + '--{0}'.format(name) + '--写入成功！\n')
        else:
            print('读取失败！')

    def html_read(self, file):
        html = etree.parse(file, parser = etree.HTMLParser(encoding = 'utf-8'))
        return html

    def csv_save(self, data,name):
        path_name = './date_{0}'.format(self.text_time()[1])
        #文件保存#
        df = pd.DataFrame(data)
        df.to_csv('{0}/{1}.csv'.format(path_name,name), index = 0, na_rep = 'NA')
    


my_rept = my_reptile()

my_rept.page_download(f'http://search.jumei.com/?filter=0-11-1&search=%E7%9C%BC%E9%9C%9C&from=search_toplist_%E7%9C%BC%E9%9C%9C_word_pos_4&cat=','testDemo.html')

