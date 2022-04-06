# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/2 12:09

# 对象的布尔值
'''
 ·Python一切姐对象,所有的对象都有一个布尔值
    ·获取对象的布尔值：使用内置函数bool()

 ·以下对象的布尔值位False：
     ·False、数值0、None、空字符串、空列表、空元组、空字典、空集合
'''

# 测试对象的布尔值
print('------以下对象的布尔值为False------')
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
print(bool(''))  # 空字符串为False
print(bool(""))  # 空字符串False
print(bool([]))  # 空列表为False
print(bool(list()))  # 空列表为False
print(bool(tuple()))  # 空元组为False
print(bool({}))  # 空字典为False
print(bool(dict()))  # 空字典为False
print(bool(set()))  # 空集合为False

print('------其它对象的布尔值均为True------')
print(bool(18))  # True
print(bool(True))  # True
print(bool('hello world'))  # True



























