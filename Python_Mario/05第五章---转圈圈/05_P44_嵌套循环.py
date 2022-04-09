# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/9 17:13
'''
     嵌套循环:循环结构中又嵌套了另外的完整循环结构,其中内层循环做为外层循环的循环体执行
    — — — — — — — — — — — — — — — — —
   |  while...:                      |
   |    ...                          |
   |     — — — — — — —               |
   |    |  for...:    |              |
   |    |    ...      |--->内层循环    | --->外层循环
   |    |  else       |              |
   |    |    ...      |              |
   |     — — — — — — —               |
   |    ...                          |
    — — — — — — — — — — — — — — — — —
'''

# 输出一个三行四列的矩形
for a in range(1,4):
    for b in range(1,5):
        print('*', end='\t')  # 不换行输出4个*
    print()  # 换行

# 打印99乘法表
for c in range(1,10):
    for d in range(1,c+1):
        print(d,'*',c,'=',c*d,end='\t')
    print()
'''输出结果
1 * 1 = 1	
1 * 2 = 2	2 * 2 = 4	
1 * 3 = 3	2 * 3 = 6	3 * 3 = 9	
1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16	
1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25	
1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36	
1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49	
1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64	
1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81
'''

# 二重循环中的break和continue用于控制本层循环
'''
     嵌套循环:循环结构中又嵌套了另外的完整循环结构,其中内层循环做为外层循环的循环体执行
    — — — — — — — — — — — — — — — — — — — — — —
   |  while...:                                |
   |    ...                                    |
   |     — — — — — — — — — — — — —             |
   |    | for...   <— — —        |             |  
   |    |   ...         ↑        |             |
   |    |   if...:      ↑        |             |
   |    |        break/continue  |--->内层循环   | --->外层循环
   |    |    ...   ↓             |             |
   |    |   else   ↓             |             |
   |    |    ...   ↓             |             |
   |     — — — — — ↓ — — — — — — —             |
   |    ...   <— — —                           |
    — — — — — — — — — — — — — — — — — — — — — —
'''
for e in range(5):
    for f in range(1,11):
        if f%3==0:  # 判断f对3的余数是否为0
            break  # 当if条件成立时,结束内层循环
        print(f,end='\t')
    print()
'''
输出结果：
1	2	
1	2	
1	2	
1	2	
1	2
'''
for g in range(5):
    for h in range(1,11):
        if h%2 == 0:  # 判断h对2的余数是否为0
            continue  # 当if条件成立时,内循环重复运行,不执行下面语句
        print(h,end='\t')
    print()
'''
输出结果：
1	3	5	7	9	
1	3	5	7	9	
1	3	5	7	9	
1	3	5	7	9	
1	3	5	7	9
'''











