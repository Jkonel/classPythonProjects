
'''
@Description: 将地区分为市和区
@Author: 李维强
@Date: 2020-06-23   11：08
'''


import pandas as pd
import numpy as np

def divide_city(original_name,save_name):
    
    
    b=pd.read_csv(original_name)
    
    city_area=b['address']
    
    city_=city_area.str.split('-').str.get(0)
    area_=city_area.str.split('-').str.get(1)

    b['city'] = city_
    b['area'] = area_
    
    df = pd.DataFrame(b)
    df.to_csv(save_name, index = 0, na_rep = 'NA')

#divide_city('all_page_salery_normalize_add_provences.csv','all_page_salery_normalize_add_provences_citys_areas.csv')
