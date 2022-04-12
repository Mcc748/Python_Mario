# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/12 11:54

'''
     列表元素的排序操作：
            1、常见的两种方式:
               ①：调用sort()方法,列表中所有元素默认按从小到大进行排序;可以指定reverse=True,进行降序排序
               ②：调用内置函数sorted(),可以指定reverse=True,进行降序排序,原列表不发生改变,产生一个新的列表
'''

#  ①：调用sort()方法,列表中所有元素默认按从小到大进行排序;可以指定reverse=True,进行降序排序
lst = [2,5,4,3,1]
print('排序前的顺序:',lst,id(lst))  # 输出:排序前的顺序: [2, 5, 4, 3, 1] 1370359294656
lst.sort()  # 默认升序排列,也可以写成: lst.sort(reverse=False)
print('排序后的顺序:',lst,id(lst))  # 输出:排序后的顺序: [1, 2, 3, 4, 5] 1370359294656
lst.sort(reverse=True)  # 使用reverse=True进行降序排列
print('排序后的顺序:',lst,id(lst))  # 输出:排序后的顺序: [5, 4, 3, 2, 1] 1370359294656

# ②：调用内置函数sorted(),可以指定reverse=True,进行降序排序,原列表不发生改变,产生一个新的列表
lst1 = [2,5,4,3,1]
print('排序前的顺序:',lst1,id(lst1))  # 输出:排序前的顺序: [2, 5, 4, 3, 1] 2597491793664
new1_lst = sorted(lst1)
print('排序后的顺序:',new1_lst,id(new1_lst))  # 输出:排序后的顺序: [1, 2, 3, 4, 5] 2597487209856
new2_lst = sorted(lst1,reverse=True)
print('排序后的顺序:',new2_lst,id(new2_lst))  # 输出:排序后的顺序: [5, 4, 3, 2, 1] 2327115492800



