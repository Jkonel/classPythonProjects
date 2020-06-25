'''
@Description: csv文件筛选函数
@Author: Jkonel
@Date: 2020-06-24 15:00:33
@LastEditors: jkonel
@LastEditTime: 2020-06-24 18:19:20
'''
import  re
import  pandas as pd

'''
@description: csv文件筛选函数
@param : 
@return: 
'''
#from data_filter import data_filter
import  re
import  pandas as pd

def data_filter(key_word, csv_file_name,save_name):
    data_frame = pd.read_csv(csv_file_name)

    rows = data_frame.shape[0]
    #print(rows)

    new_data = pd.DataFrame()
    for i in range(0, rows):
        a = data_frame.iloc[i,]
        title = a['title']
        judge = re.findall(key_word, title)
        if judge:
            new_data = new_data.append(a)
    new_data.to_csv(save_name, index=0, na_rep='NA')



data_filter(r'嵌入式','./projects_multperson/date_2020-6-23/embeded_software_salary_norm_add_provence_city_area_del_none.csv','result_embeded_software.csv')



