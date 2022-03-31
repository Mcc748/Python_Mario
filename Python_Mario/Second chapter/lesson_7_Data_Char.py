# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/27 22:01

#  ·1、二进制与字符编码
#     使用0和1来表示的计算机语言，所有的字符都有相对应的字符编码（Unicode几乎包含全世界的字符）
print(chr(0b100111001011000))  # 0b表示二进制
print(ord('乘'))  # 使用ord查找文字的十你进制语言

#  ·2、Python中的标识符与保留字
#     保留字：Python程序中有些单词被赋予了特定的意义，不可以使用其命名
import keyword
print(keyword.kwlist)
#     标识符：给变量、函数、类、模块和其它对象起的名字就叫标识符.
#     标识符规则：1、不能以数字开头.  2、不能是我的保留字.   3、严格区分大小写


#  ·3、Python中的变量与数据类型
#     变量就是自定义的一个名字，可以存储需要的数据
#    变量由三部分组成
#     ·标识：表示对象所存储的内存地址,使用内置函数id（obj）来获取.
#     ·类型：表示的是对象的数据类型,使用内置函数type（obj）来获取.
#     ·值：表示对象所存储的具体数据,使用print（obj）可将值直接进行打印输出.
name = '玛丽亚'  # name为变量, =为赋值运算符, 玛丽亚为值
print(name)  # 可直接输出变量
print('标识', id(name))  # ---->‘玛丽亚’的存储地址
print('类型', type(name))  # ---->’玛丽亚‘的字符类型
print('值', name)

#    数据类型
#    ·整数类型 ---> int ---> 100 注：可以表示正数负数和零,二进制以0b开头,八进制以0o开头,十六进制以0x开头
n1 = 0
n2 = -76
n3 = 90
n4 = 0b0100
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
print(n4, type(n4))

#    ·浮点数类型 ---> float ---> 3.1415926
a = 3.1415926
print(a, type(a))
#      浮点数的运算可能会出现不确定的情况，解决方案为导入decimal模块
print(1.1 + 2.2)  # 结果等于3.3000000000000003
#   导入decimal模块
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

#    ·布尔类型 ---> bool ---> True（真）,False（假） 注：判断一个事物的真假，结果为真则是true，反之为false
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))
#   布尔值可以转成整数计算的
print(f1 + 1)  # 1+1的结果为2
print(f2 + 1)  # 0+1的结果为1

#    ·字符串类型 ---> str ---> ‘人生苦短,我用Python’
#       1> 可以使用单引号'嗨', 双引号”嗨 “,三引号'''嗨'''或"""嗨"""来定义
#       2> 单引号双引号定义的字符必须在一行
#       3> 三引号定义的字符串可以分布在连续的多行
str1 = '人生苦短,我用Python'
str2 = "人生苦短,我用Python"
str3 = '''人生苦短,
我用Python'''

str4 = """人生苦短,
我用Python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))



