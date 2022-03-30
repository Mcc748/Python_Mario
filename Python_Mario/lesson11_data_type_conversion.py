# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/30 10:34

# 数据类型转换
# ·为什么需要数据类型转换？
#    ·将不同数据类型的数据拼接在一起
#  1> str() ---> 将其它数据类型转换成字符串 ---> str(123)得到'123' ---> 注意：也可用引号转换
#  2> int() ---> 将其它数据类型转换成整数 ---> int('123')得到123 ---> 注意：文字和小数类字符无法转换成整数,浮点数抹零取整
#  3> float() ---> 将其它数据类型转换成浮点数 ---> float('9')得到9.0 ---> 注意：文字无法转换,整数末尾为.0

name = '马里奥'
age = 20
print(type(name), type(age))  # 输出两个数据类型
#  print('我叫' + name + '今年' + age + '岁')  # （加号为连接符）当将str类型与int类型进行连接时,报错！！解决方案：类型转换
print('我叫' + name + ',今年' + str(age) + '岁')  # 将int类型通过str()函数转成了str数据类型

print('----------str():将其它类型转成str类型------------')
a = 10
b = 198.8
c = False  # 布尔类型数据
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

print('-----------int():将其它类型转成int类型------------')
s1 = '128'
f1 = 98.7
s2 = '77.77'
f2 = 'Mario'
ff = True
print(type(s1), type(f1), type(s2), type(f2), type(ff))
print(int(s1), type(int(s1)))    # 将str转换成int类型,字符串为数字串
print(int(f1), type(int(f1)))    # float转成int类型,只取整数部分
# print(int(s2), type(int(s2)))  # 将str转换成int类型,报错,因为字符串为小数
# print(int(f2), type(int(f2)))  # 将str转成int类型时，字符串必须为整数
print(int(ff), type(int(ff)))    # 布尔类型可进行转换

print('-----------float():将其它类型转成float类型------------')
s3 = '128.98'
f3 = '76'
s4 = 10
f4 = 'Mario'
cc = True
print(type(s3), type(f3), type(s4), type(f4), type(cc))
print(float(s3), type(float(s3)))
print(float(f3), type(float(f3)))
print(float(s4), type(float(s4)))
# print(float(f4), type(float(f4)))  #  字符串中的数据非数字串，则不能进行转换
print(float(cc), type(float(cc)))


























