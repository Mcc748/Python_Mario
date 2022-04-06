# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/6 21:01

# 条件表达式
'''从键录入两个整数，比较两个整数的大小'''
print('输入两个整数比较大小')
num1 = int(input('请输入第一个整数：'))
num2 = int(input('请输入第二个整数：'))

# 第一个比较方式
'''
if num1 >= num2:
    print(num1, '大于等于', num2)
else:
    print(num1, '小于', num2)
'''

# 第二个比较方式
# print((num1, '大于等于', num2) if num1 >= num2 else (num1, '小于', num2)) # 结果：(20, '大于等于', 5）,这种方式输出不好看
print(str(num1)+'大于等于'+str(num2) if num1 >= num2 else str(num1)+'小于'+str(num2))  # 使用字符串的连接
# 条件判断的结果为True则输出右侧,如果条件判断的结果为False则输出左侧
