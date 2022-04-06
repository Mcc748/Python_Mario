# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/6 21:52

# range函数的使用
'''
range()函数
       1> 用于生成一个整数序列
                                 --- 2.1：range(stop) ---> 创建一个【0，stop】之间的整数序列,步长为1
       2> 创建range对象的三种方式：  --- 2.1：range(start,stop) ---> 创建一个【start,stop】之间的整数序列,步长为1
                                 --- 2.1：range(start,stop,step) ---> 创建一个【start,stop,step】之间的整数序列,步长为1
       3> 返回值是一个迭代器对象
       4> range类型的优点：不管range对象表达式的整数序列有多长,所有range对象占用的内层空间都是相同的，因为仅仅需要存储start、stop
                         和step. 只有当用到range对象时,才会去计算序列中的相关元素.
       5> in与not in判断整数序列中是否存在（不存在）指定的整数
'''

# range的三种创建方式如下：

# 第一种创建方式
a = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  默认从0开始，但结果不包含10,默认步长为1
print(a)  # 输出：range(0, 10)  得到一个区间范围
print(list(a))  # 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  得到对象的整数序列 ---> list为列表的意思

# 第二种创建方式
b = range(2, 10)  # [2, 3, 4, 5, 6, 7, 8, 9]  默认从0开始,但结果不包含10,默认步长为1
print(list(b))  # 输出：[2, 3, 4, 5, 6, 7, 8, 9]

# 第三种创建方式
c = range(1, 10, 2)  # 输出：[1, 3, 5, 7, 9]  默认从1开始,默认步长为2
print(list(c))  # 输出：[1, 3, 5, 7, 9]


# 判断指定的整数是否在序列之中,使用：in 或 not in
d = range(10)
print(10 in d)  # 输出：False
print(8 in d)  # 输出：True

print(11 not in d)  # 输出：True
print(5 not in d)  # 输出：False








