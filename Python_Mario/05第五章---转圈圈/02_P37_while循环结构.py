# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/6 22:27

# while循环结构
'''
       1> 反复做同一件事情的情况,称为循环
       2> 循环结构的流程：如果条件表达式一直为True则一直执行循环体,直到条件表达式为False时结束条件循环体
       3> 循环的分类：①、while  ②、for-in
       4> 语法结构：
                 while 条件表达式:
                       条件执行体（循环体）
       5> 选择结构的if与循环结构while的区别
          ①、if是判断一次,条件为True执行一行
          ②、while是判断n+1次,条件为True执行n次
'''

a = 1
while a < 10:  # 条件表达式
    # 条件执行体
    print(a)
    a += 1

# 计算0-10之间的累加和
b = 1
c = 0
while b < 10:
    c += b
    b += 1
print('和为：', c)

# 计算1-100之间的偶数和
# 方法1
sum1 = 0
e = 0
while e < 100:
    sum1 += e
    e += 2
print('1至100之间的偶数和为：', sum1)

# 方法2
sum2 = 0
f = 0
while f < 100:
    if f % 2 == 0:  # 条件判断是否为偶数
#   if not bool(f%2):   #使用布尔值取反也可判断是否为偶数
        sum2 += f
    f += 1
print('1至100之间的偶数和为：', sum2)

























































