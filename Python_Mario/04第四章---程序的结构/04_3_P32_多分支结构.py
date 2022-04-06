# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/2 14:30

# 多分支结构
'''
  if 条件表达式：
      条件执行体1
  elif：
      条件执行体2
  elif：
      条件执行体3
  elif：
      条件执行体4
          .
          .
          .
   else:
       条件执行语句N
'''

print('---判断分数在哪个分段---')
'''
输入一个整数成绩
90-100 A
80-89  B
70-79  C
60-69  D88
0-59   E10
小于0或者大于100不是成绩的有效范围
'''
num = int(input('请输入一个整数成绩'))
if 90 <= num <= 100:
    print(num, '这个分数为A')
elif 80 <= num < 90:
    print(num, '这个分数为B')
elif 70 <= num < 80:
    print(num, '这个分数为C')
elif 60 <= num < 70:
    print(num, '这个分数为D')
elif 0 <= num < 60:
    print(num, '这个分数为E')
else:
    print(num, '不是一个有效成绩')
