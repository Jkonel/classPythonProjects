<!--
 * @Description: classPythonProjects
 * @Author: Jkonel
 * @Date: 2020-06-10 14:11:59
 * @LastEditors: jkonel
 * @LastEditTime: 2020-06-10 16:59:42


# classPythonProjects
All my python projects during class.  
1. Python 运算符  
    //： 整除  
    / ： 自然除  
    **:  幂次  
    python没有++，--；有—=，+=  
    python不支持连续运算逻辑组合，慎用()[]{}  
    
--> 


<!--
 * @Description: classPythonProjects
 * @Author: Jkonel
 * @Date: 2020-06-10 14:11:59
 * @LastEditors: jkonel
 * @LastEditTime: 2020-06-10 15:11:40
--> 

# classPythonProjects

1. jupyter 使用教程  
    1. 两种操作模式的切换  
        代码模式  ESC + y  
        笔记模式  ESC + m  
    2. 运行  
        ctrl+enter  运行代码  
        alt+ enter  运行代码并新建一个新的输入框  
    3. 修改输入框的内容，需要双击输入框     
    4. jupyter 常用快捷键  
       >*ESC+A 在当前输入框上面插入一个新的输入框  
        *ESC+B 在当前输入框下面插入一个新的输入框  
        ESC+C 复制当前的输入框  
        ESC+V 粘贴当前的输入框  
        ESC+X  剪切当前的输入框  
        ESC+ DD  删除当前的输入框  
        ESC+Z 撤销上一次删除操做  
        ESC+H 查看帮助文档  
    

2. Markdown  
    1. 标题  
        # 标题一  
        ## 标题二  
        ### 标题三  
    2. 有序列表  
        在行首增加 1.、2.、3.，即数字和英文句点, 注意句点与文字中间有空格。 
        1. 第一点  
        2. 第二点  
        3. 第三点  
    3. 无序列表  
        在行首增加 * 或 -  
        - 1 
        - 2 
        - 3  
    4. 引用  
        文字前添加 '>'   
        > 这是一条引用    
    5. 超链接

        [百度](https://www.baidu.com)  
    
    6. 分割线   
        ---  
        
        ***  
    7. 代码  
          一次缩进是内容，二次缩进是文本（不会执行其中的标签指令）  

3. Python 笔记  
    1. 入门  
        1. 输入和输出语句  
            > input  
              print  
        2. 注释 #  

    2. 变量  

        * 数字 字符串 布尔

            类型分别为 : int  float str bool（True False）

            类型转化函数为： int()  float() str() bool()

        > python 是一种弱类型的语言  
        python 是一种简单易学的语言  
        python 是一种容易扩展、功能强大的语言  

       *  变量名命名规则  见名知义  per_increase
                
    3. 运算符-算数
    
        1. 常规运算符
    
                + - * /  
            
            >  * 不寻常: //  %  **  
                // 表示整除  
                % 表示取余数  
                ** 表示幂运算    
                
        2. 关系运算符
            
                > < >= <= == !=  
            
        3. 逻辑运算符 
        
                and not or
    
            > 运算的结果一定是bool
            
        4. 成员运算符
            in not in  
            > *说明:  
                1. python中没有 ++ --  
                2. python 可以用 x [1,100]   可以写成  1<=x<=100  建议写成 x>=1 and x<=1000  
                3. 可以用复合运算符  
            
        5. 判断语句    
            > n=150 
            if n>100:  
                print(f'{n} 大于100')  
            else:   
                print(f'{n} 小于100')  
                print('end')  
        
            > *特点：  
                1. 每条分支语句用冒号结束
                2. 不用分号表示语句结束
                3. 用缩进表示代码范围(注意缩进用tab键)
                4. 条件不用小括号
        6. pass 语句  
            永远占位  
        7. 循环
            > s='python'  
            for i in s:  
                print(i)  
            
            > *特点：
                1. 冒号
                2. 缩进
                3. 没有分号
                4. i 临时变量
                5. for 本质上是一种遍历行为
