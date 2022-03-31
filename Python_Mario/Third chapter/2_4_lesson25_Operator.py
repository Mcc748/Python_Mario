# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/30 20:20

# 布尔运算符
'''
          1> and   当两个运算数都为真时,运算结果才为True
          2> or    只要有一个运算数为真时,运算结果就为True
布尔运算符  3> not   如果运算数为True,则结果为False
          4> in    检查字符是否在字符串中,在为True,不在为False
          5> not in 检查字符是否在字符串中,在为False, 不在为True
'''

# 1> and   当两个运算数都为真时,运算结果才为True
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 1 and b < 2)  # False

# 2> or    只要有一个运算数为真时,运算结果就为True
print(a == 1 or b != 2)  # True
print(a != 1 or b != 2)  # False

# 3> not   如果运算数为True,则结果为False,用于对布尔类型的操作数取反
f1 = True
f2 = False
print(not f1)  # False
print(not f2)  # true

# 4> in 和 not in 检查字符是否在字符中
s = 'hello world'
print('w' in s)  # True  w在s字符串中时为True
print('k' in s)  # False  k不在s字符串中时为False
print('w' not in s)  # False  w在s字符串中时为False
print('k' not in s)  # True   k在s字符串中时为True
