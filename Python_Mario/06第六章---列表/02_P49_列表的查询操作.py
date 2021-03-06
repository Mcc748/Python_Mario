# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/10 16:40

'''
     列表的查询操作：
            1、获取列表中指定元素的索引:
                         ①：如果查寻列表中存在N个相同元素,只返回相同元素中的第一个元素的索引
               index() : ②：如果查询的元素在列表中不存在,则会抛出ValueError
                         ③：还可以在指定的start和stop之间进行查找
'''

lst = ['hello','Mario',2333,'Mario',666,'hello']
print(lst.index('Mario'))  # 输出：1 ---> 列表中有多个相同元素,结果只输出第一个元素的位置

# print(lst.index('Python'))  # 输出：ValueError: 'Python' is not in list

# 可指定区间索引元素
# print(lst.index('hello',1,4))  # 输出ValueError: 'hello' is not in list


'''
            2、获取列表中的单个元素
                          ①：正向索引从左到右,0开始    举例：lst[0]   ---> 获取第一个元素
               获取单个元素：②：逆向索引从右到左,-1开始   举例：lst[-1]  ---> 获取最后一元素
                          ③：指定索引如果不存在,抛出IndexError
'''

lst1 = ['hello','Mario',2333,'Mario',666,'hello']
# 获取索引为2的元素:索引为2指的是列表中的第三个元素
print(lst1[2])  # 输出：2333
print(lst1[-4])  # 输出：2333
# 获取索引为10的元素
# print(lst1[10])  # 输出：IndexError: list index out of range  ---> list超出范围

'''
   3、获取列表中的多个元素
      语法格式：列表名[start:stop:step]      
         
              ①：切片的结果 ---> 原列表片段的拷贝
      切片操作：②：切片的范围 ---> [start,stop]
              ③：step默认为1 ---> [start:stop]
              ④：step为正数：
                    1.[:stop:step] ---> 切片的第一个元素默认是列表的第一个元素 ---> 从start开始往后计算切片
                    2.[start::step] ---> 切片的最后一个元素默认是列表的最后一个元素 ---> 从start开始往后计算切片
              ⑤：step为负数：
                    1.[:stop:step] ---> 切片的第一个元素默认是列表的最后一个元素 ---> 从start开始往后计算切片
                    2.[start::step] ---> 切片的最后一个元素默认是列表的第一个元素 ---> 从start开始往前计算切片
'''
# 顺序   0  1  2  3  4  5  6  7
lst2 = [10,20,30,40,50,60,70,80]
print(lst2[1:6:1])  # 输出：[20, 30, 40, 50, 60] ---> 从顺序1开始,到5结束,不包含6
print(lst2[1:6])  # 输出：[20, 30, 40, 50, 60] ---> 默认步长为1
print(lst2[1:6:])  # 输出：[20, 30, 40, 50, 60] ---> 默认步长为1
print(lst2[1:6:2])  # 输出：[20, 40, 60] ---> 默认步长为2
print(lst2[:6:2])  # 输出：[10, 30, 50] ---> 从0开始,步长为2
print(lst2[1::2])  # 输出：[20, 40, 60, 80] ---> 到7结束,步长为2
print('new',lst2[6:1:-1])  # 输出：[70, 60, 50, 40, 30] ---> 从顺序6开始,到1结束,不包含1
lst3 = lst2[1:6:1]
print('原列表id:',id(lst2))  # 输出：原列表id: 2663329914688
print('新列表id:',id(lst3))  # 输出：新列表id: 2663329590656

'''
   4、列表元素的查询操作
      ①、判断指定元素在列表中是否存在：
               元素 ---> in ---> 列表名
               元素 ---> not in ---> 列表名
      ②、列表元素的遍历：
               for 迭代变量 in 列表名：
                      操作
'''
# ①、判断指定元素在列表中是否存在
lst4 = [10,20,'python','Mario']
print(10 in lst4)  # 输出：True
print(10 not in lst4)  # 输出：False
print(100 in lst4)  # 输出：False
print(100 not in lst4)  # 输出：True

# ②、列表元素的遍历
lst5 = [10,20,'python','Mario']
for item in lst5:
    print(item)  # 依次输出：10、20、python、Mario

