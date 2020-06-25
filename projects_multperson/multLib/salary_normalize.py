'''
@Description: 薪资统一为月薪
@Author: 李维强
@Date: 2020-06-23 
'''

import re
import pandas as pd
import  numpy as np


def sal(original_name,save_name):
    c=pd.read_csv(original_name)
    

    salarys = c['salery']
    reg_sa=r'\d+(?:\.\d+)?'
    
    print(salarys)

    salary_min = []
    salary_max =[]
    
    for sa in salarys:
        #print(sa)
        if sa is not np.nan :
            r=re.findall(reg_sa,sa)
            dict={ }
            if '万/月' in sa:
                sa_min=float(r[0])*10000
                sa_max=float(r[1])*10000
            elif '千/月' in sa:
                sa_min=float(r[0])*1000
                sa_max=float(r[1])*1000
            elif '万/年' in sa:
                sa_min=float(r[0])*10000//12
                sa_max=float(r[1])*10000//12
            elif '' in sa:
                sa_min=None
                sa_max=None
                
            salary_min.append(sa_min)
            salary_max.append(sa_max)
        else:
            salary_min.append(np.nan)
            salary_max.append(np.nan)
            continue
       
    c['salary_min'] = salary_min
    c['salary_max'] = salary_max
    
    df = pd.DataFrame(c)
    df.to_csv(save_name, index = 0, na_rep = 'NA')


#sal('.//all_page.csv','all_page_salery_normalize.csv')


