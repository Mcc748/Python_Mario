# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/30 15:41

# ③、比较运算符：对变量或表达式的结果进行大小、真假等比较.比较的结果为布尔类型

'''
          1>: 符号有 > , < , >= , <= , !=
比较运算符: 2>: 对象value的比较： ==
          3>: 对象id的比较： is , is not
'''

a, b = 10, 20
print('a>b吗？', a > b)  # 结果：False
print('a<b吗？', a < b)  # 结果：true
print('a>=b吗？', a >= b)  # 结果：False
print('a<=b吗？', a <= b)  # 结果：true
print('a==b吗？', a == b)  # 结果：False
print('a!=b吗？', a != b)  # 结果：true

'''
一个 = 为赋值运算符,两个 == 为比较运算符
一个变量由三部分组成：标识、类型、值
== 比较的是变量的值
比较对象的标识使用 is , is not
'''
a = 10
b = 10
print(a == b)  # 结果为：true  说明：a和b的value相等
print(a is b)  # 结果为：true  说明：a和b的id标识相等
print(a is not b)  # 结果为：False
# 以下为值相同的list进行比value和id
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)  # 比较的value结果为：True
print(list1 is list2)  # 比较的id结果为：False
print(list1 is not list2)  # 比较的id结果为：True
print(id(list1))  # 结果id为：2150544726976
print(id(list2))  # 结果id为：2150544726656
