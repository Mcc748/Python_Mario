# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/11 16:12

'''
            1、列表元素的增加操作
                           方法/其它
                           append() ------> 在列表的末尾添加一个元素
                增加操作:    extend() ------> 在列表的末尾至少添加一个元素
                           insert() ------> 在列表的任意位置添加一个元素
                             切片  --------> 在列表的位置添加至少一个元素
'''

# append() ------> 在列表的末尾添加一个元素,列表的id保持不变
lst = [10,20,30]
print('添加元素前：',lst,id(lst))  # 输出: 添加元素前： [10, 20, 30] 2293256841920
lst.append(100)
print('添加元素后：',lst,id(lst))  # 输出: 添加元素后： [10, 20, 30, 100] 2293256841920
# 将一个列表添加到另一个列表的末尾,原列表id保持不变
lst1 = ['hello','world']
lst.append(lst1)
print('添加lst1:',lst,id(lst))  # 输出: 添加lst1: [10, 20, 30, 100, ['hello', 'world']] 2522832136896

# extend() ------> 在列表的末尾一次添加多个元素
lst2 = ['hello','world']
lst3 = [10,20,30]
lst3.extend(lst2)
print('添加多个元素:',lst3)  # 输出: 添加多个元素: [10, 20, 30, 'hello', 'world']

# insert() ------> 在列表的任意位置添加一个元素
lst4 = [10,20,'hello',40]
lst4.insert(1,'mario')
print('在10的后面添加元素：',lst4)  # 输出: 在10的后面添加元素： [10, 'mario', 20, 'hello', 40]

# 切片  --------> 将原列表指定区域进行覆盖,添加至少一个元素,id保持不变
lst5 = [10,20,'go',30,40]
print('原列表:',lst5,id(lst5))  # 输出: 原列表: [10, 20, 'go', 30, 40] 1968100557312
lst6 = ['mario',233,666]
lst5[1:3]=lst6  # 将1、2位置的进行切片覆盖
print('切片后的新列表:',lst5,id(lst5))  # 切片后的新列表: [10, 'mario', 233, 666, 30, 40] 1968100557312


'''
            2、列表元素的删除操作
                           方法/其它
                           remove() ------> 一次只删除一个元素;重复元素只删除第一个;元素不存在时抛出ValueError
                删除操作:    pop() ------> 删除一个指定索引位置上的元素;指定索引不存在抛出IndexError;不指定索引,删除最后一个元素
                           切片  --------> 一次至少删除一个元素
                           clear() ------> 清空列表
                           del   ----> 删除列表
'''

# remove() ------> 一次只删除一个元素;重复元素只删除第一个;元素不存在时抛出ValueError
lst7 = [10,20,30,40,50,60,20]
lst7.remove(20)
print(lst7)  # 输出:[10, 30, 40, 50, 60, 20] ---> 从列表移除一个元素,有重复只移除第一个元素

# pop() ------> 删除一个指定索引位置上的元素;指定索引不存在抛出IndexError;不指定索引,删除最后一个元素
lst8 = [10,20,30,40,50,60,]
lst8.pop(1)  # 移除索引位置1上面的元素
print(lst8)  # 输出: [10, 30, 40, 50, 60]
lst8.pop()   # 未指定位置移除最后一个元素
print(lst8)  # 输出: [10, 30, 40, 50]

# 切片  --------> 一次至少删除一个元素,id变更
lst9 = [10,20,30,40,50,60,]
print('原列表',lst9,id(lst9))  # 输出: 原列表 [10, 20, 30, 40, 50, 60] 2246106825856
new_lst9 = lst9[1:4]  # 取出区间内的列表,id变更
print('切片后的列表',new_lst9,id(new_lst9))  # 输出: 切片后的列表 [20, 30, 40] 2246106825984
lst9[1:3] = []  # # 删除区间外的列表,id不变
print('原列表',lst9,id(lst9))  # 输出:切片后的列表 [10, 40, 50, 60] 2246106825856

# clear() ------> 清空列表
lst10 = [10,20,30,40,50,60,]
lst10.clear()
print(lst10)  # 输出: []
del lst10
# print(lst10)  # 输出: NameError: name 'lst10' is not defined ---> 列表不存在


'''
            2、列表元素的修改操作
                ①、为指定索引元素赋予一个新值
                ②、为指定切片赋予一个新值
'''
# ①、为指定索引元素赋予一个新值
lst11 = [10,20,30,40,50]
print('id:',id(lst11))  # 输出:   id: 2131042252352
lst11[2]='mario'
print(lst11,'id:',id(lst11))  # 输出: [10, 20, 'mario', 40, 50] id:id: 2131042252352

# ②、为指定切片赋予一个新值
lst12 = [10,20,30]
print('id:',id(lst12))  # 输出:  id: 2202160167808
lst12[1:2] = ['hello','good','man']
print(lst12,'id:',id(lst12))  # 输出:[10, 'hello', 'good', 'man', 30] id: 2202160167808


