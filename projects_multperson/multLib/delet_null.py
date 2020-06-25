'''
@Description: 删除空值
@Author: 李维强
@Date: 2020-06-23   12：02
'''

import pandas as pd

def delete_null(file_name, res_name):
    all_date = pd.read_csv(file_name)
    #not_null = all_date.dropna()    # 去空
    not_null = all_date.dropna(axis = 0,subset = ['title','company','address','salery','date','salary_min','salary_max','provence','city'])   # 丢弃指定列中有缺失值的行
    not_null.to_csv(res_name, index = 0)


#delete_null('./projects_multperson/all_page_salery_normalize_add_provences_citys_areas.csv','all_page_salery_normalize_add_provences_citys_areas_delete_null.csv')
