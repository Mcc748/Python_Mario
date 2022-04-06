# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/6 21:29

# pass语句
'''
pass语句什么都不做,只是一个占位符,用在语法上需要语句的地方

什么时候使用pass语句：
    先搭建语法结构,还没想好代码怎么写的时候

和那些语句一起使用：
   1> if语句的条件执行体
   2> for-in语句的循环体
   3> 定义函数时的函数体
'''

c = input('您是会员吗？y/n')

# 判断是否是会员
if c == 'y':
    pass
else:
    pass

# if可以直接判断布尔值（可直接把表达式放在条件表达式上做判断）
age = int(input('请输入你的年龄：'))
if age:
    print(age)  # 如果输入的数字布尔值为True时,输出'age值'
else:
    print('您的年龄为：', age)  # 如果输入的数字布尔值为False时,输出'您的年龄为：age值'

