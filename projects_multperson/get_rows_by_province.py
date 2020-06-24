'''
@Description: 从数据矩阵中根据特定列的特定关键字提取全部符合的行数据
@Author: Jkonel
@Date: 2020-06-24 09:15:17
@LastEditors: jkonel
@LastEditTime: 2020-06-24 09:25:42
'''

def get_rows_by_province(data_frame,name_row, name_keyword):
    res = data_frame.loc[data_frame[name_row]==name_keyword]
    return res

