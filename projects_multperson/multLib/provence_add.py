'''
@Description: 将每个地区转化为省份
@Author: 陈旭，季洪坤
@Date: 2020-06-23 
'''

from city2provence import city2provence
from city2provence import city_get
import pandas as pd


def provence_add(original_name,save_name):
    
    c=pd.read_csv(original_name)
    
    prov = c['address']
    provences=[]
    
    for addr in prov:   
        prove = city2provence(city_get(addr))
        provences.append(prove)

    c['provence'] = provences
    
    df = pd.DataFrame(c)
    df.to_csv(save_name, index = 0, na_rep = 'NA')

#provence_add('all_page_salery_normalize.csv','all_page_salery_normalize_add_provences.csv')
 