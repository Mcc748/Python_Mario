# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/27 18:50

# print() 函数的使用

# print()函数可以输出那些内容？？？
# ·（1）函数输出的内容可以是数字,不需要添加单引号
print(520)
print(10.5)

# ·（2）函数输出的内容可以是字符串，需要添加单引号
print('Hello world')

# ·（3）函数输出的内容可以是含有运算符的表达式
print(3 + 1)

# print()函数可以将内容输出的目的地
#  ·（1）将数据输出到显示器（下方运行的控制台）
print(520)

#  ·（2）将数据输出到文件中;注意：1.所指定的盘符必须存在。 2.使用 file= fp
fp = open('C:/Users/Mcc/Desktop/Python/Python_Mario/text.txt',
          'a+')  # C：/...指输出路径; a+指以读写的方式打开文件，文件不存在则创建文件，存在则在原有的文件上追加内容
print('Hello world', file=fp)
fp.close()

# print()函数的输出形式
#  ·（1）换行 ：可使用反斜杠+n
#  ·（2）不进行换行输出（输出内容在一行）
print('Hellow', 'World', 'Python')
