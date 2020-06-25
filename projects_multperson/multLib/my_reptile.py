'''
@Description: 爬虫提取参考类
@Author: Jkonel
@Date: 2020-06-18 09:15:14
@LastEditors: jkonel
@LastEditTime: 2020-06-22 17:13:10
'''

import requests
from lxml import etree
import pandas as pd
import re
from datetime import datetime
import time
import os
import chardet


class my_reptile:
    def __init__(self):
        pass
    
    '''
    @description: 时间戳方法
    @Author: Jkonel
    @param : self
    @return: 微秒，天，分钟
    '''
    def text_time(self):
        #[毫秒，日，分钟]
        tim = time.time()
        res = datetime.fromtimestamp(tim) 
        strc_exact = '{0}-{1}-{2}-{3}_{4}_{5}_{6}'.format(res.year, res.month, res.day, res.hour, res.minute, res.second, res.microsecond)
        strc_day = '{0}-{1}-{2}'.format(res.year, res.month, res.day)
        strc_min = '{0}-{1}-{2}-{3}_{4}'.format(res.year, res.month, res.day, res.hour, res.minute)
        return [strc_exact, strc_day, strc_min]
    
    '''
    @description: 字符串数字提取
    @Author: Jkonel
    @param : stri
    @return: nums
    '''
    def get_nums(self, stri):
        res = re.findall(r'\d[?:\d\.]\d+?', stri)
        return float(res)#bug
    
    '''
    @description: 提取文件夹下所有文件名
    @auther:jkonel
    @param : folder
    @return: name list
    '''
    def get_files_name(self, folder):
        #print(list(os.walk(folder)))
        return list(os.walk(folder))[0][2]
    
    '''
    @description: 文件编码检测
    @param : filename
    @return: encoding_info
    '''
    def check_code(self, filename):
        bytes_data = open(filename,mode = 'rb').readline()
        encoding_info = chardet.detect(bytes_data)['encoding']
        return encoding_info
    
    '''
    @description: 网页爬虫下载
    @Author: Jkonel
    @param : url, page name
    @return: download page
    '''
    def page_download(self, url, name):
        # url:网址；name：保存名字
        headers = {'user-agent': 'Mozilla/5.0'}
        path_name = './date_{0}'.format(self.text_time()[1])
        log_name = '{0}/log_{1}.txt'.format(path_name,self.text_time()[2])

        if not os.path.isdir(path_name):
            os.mkdir(path_name)
        if not os.path.isfile(log_name):
            with open(log_name,'w') as pp:
                pp.write('{0}/日志记录:{1}:\n'.format(path_name,self.text_time()[0]))

        respond = requests.get(url, headers=headers)

        if respond.status_code == 200:
            with open('{0}/{1}'.format(path_name,name),'w',encoding = respond.encoding) as fp:
                fp.write(respond.text)
            with open(log_name,'a') as pp:
                pp.write(self.text_time()[0] + '--{0}'.format(name) + '--写入成功！\n')
        else:
            print('读取失败！')

    #def html_read(self, file):
        ##path_name = './date_{0}'.format(self.text_time()[1])
        #html = etree.parse(file, parser = etree.HTMLParser(encoding = 'utf-8'))
        #return html
    
    '''
    @description: 网页内容提取写出(写出文件名列表所有数据，数据提取以51jobs为例，便重载)
    @auther:jkonel
    @param:folder name, htnl name, csv name
    @example: web_parsing('./demo',files_name_list,'csv_name.csv')
    @return: none
    '''
    def web_parsing(self,path_name, names_html, name_csv):
        dat = []
        for i in names_html:
            #name = 'page_1_{0}.html'.format(i)
            #path_name = './demo'  #文件夹名字demo,解析python网页
            try:
                with open(path_name +'/'+ i, 'r') as f:
                    c = f.read()
            except UnicodeDecodeError:
                with open(path_name +'/'+ i, 'r',encoding='utf-8') as f:
                    c = f.read()
            
            html = etree.HTML(c)
            
            items = html.xpath('//div[@class = "dw_table"]/div[@class = "el"]')
            #print(items)
            #-------------------文件解析------------------#
            for item in items:
                dic = {}
                
                title = item.xpath('.//p/span/a/@title')
                company = item.xpath('.//span[@class = "t2"]/a/text()')
                address = item.xpath('.//span[@class = "t3"]/text()')
                salery = item.xpath('.//span[@class = "t4"]/text()')
                date = item.xpath('.//span[@class = "t5"]/text()')
                
                if title:
                    title = title[0]
                else:
                    title = None

                if company:
                    company = company[0]
                else:
                    company = None

                if address:
                    address = address[0]
                else:
                    address = None

                if salery:
                    salery = salery[0]  #my_rep.get_nums(salery[0])
                else:
                    salery = None

                if date:
                    date = date[0]
                else:
                    date = None

                dic['title'] = title
                dic['company'] = company
                dic['address'] = address
                dic['salery'] = salery
                dic['date'] = date

                dat.append(dic)
        #---------------文件保存----------------#
        self.csv_save(dat, name_csv)

    '''
    @description: csv文件写出
    @auther:jkonel
    @param : csv data, csv name
    @return: none
    '''
    def csv_save(self, data, name):
        path_name = './date_{0}'.format(self.text_time()[1])
        if not os.path.isdir(path_name):
            os.mkdir(path_name)
        df = pd.DataFrame(data)
        df.to_csv('{0}/{1}'.format(path_name,name), index = 0, na_rep = 'NA')
    
