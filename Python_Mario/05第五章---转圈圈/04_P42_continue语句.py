# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/9 16:35

'''
     continue语句:用于结束循环语句,进入下依次循环,通常和分支结构if一起使用

    for ... in ... :    <-------                  while (条件):   <-------
          ...                  |                      ...               |
          if ... :             |                     if ... :           |
            continue  ----------                        continue  -------
          ...                                        ...
'''

print('----使用continue找出0-50中能被5整除的数----')

# 不使用continue的方法:和5相除余数为零的数都是5的倍数
for item in range(1,51):
    if item%5 == 0:
        print(item)  # 输出：5、10、15、20、25、30、35、40、45、50

# 使用continue的方法:和5相除且余数不为零的数都不是5的倍数
for item1 in range(1,51):
    if item1%5 != 0:
        continue  # 余数不为零返回for语句再次运行
    print(item1)  # 输出：5、10、15、20、25、30、35、40、45、50




















