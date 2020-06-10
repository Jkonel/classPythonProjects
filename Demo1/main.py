'''
@Description: main.py
@Author: Jkonel
@Date: 2020-06-10 09:19:55
@LastEditors: jkonel
@LastEditTime: 2020-06-10 15:13:04
'''
import math

print('test Demo 1')
#a = input('input name:')   #input输入字符串
#a = int(input('input name:'))
a = 'hello'
b = True
c = 3.1415

d = round(c)  #四舍五入转换
e = math.floor(c)   #down
f = math.ceil(c)    #up

print('年龄：'+str(d))  ##类型转换
print('test{1},test{0}'.format(1, 2))   #对象属性运用

#运算符
a = 2 * 5
b = 2 ** 5
print(a, b)

try:
    a = int(input('age:'))
except ValueError:
    a = -1
a >= 0 and a <= 100 and print(a)
