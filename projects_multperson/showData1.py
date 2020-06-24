'''
@Description: 
@Author: Jkonel
@Date: 2020-06-23 19:52:19
@LastEditors: jkonel
@LastEditTime: 2020-06-23 20:00:38
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

cols2=['title','provence','salary_min','salary_max']
folder = './projects_multperson/date_2020-6-23/'
files_list = my_rep.get_files_name(folder)


data = [
]

for i in files_list:

    jobs = pd.DataFrame(folder +'/'+ i,columns=cols2)
    
