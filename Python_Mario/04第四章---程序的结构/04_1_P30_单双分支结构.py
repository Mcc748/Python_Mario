# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/2 14:08

# 单分支结构（图片）
'''
  if 条件表达式：
      条件执行体
'''

money = 1000  # 余额
s = int(input('请输入取款金额'))  # 取款金额
if money >= s:  # 判断余额是否充足
    money = money - s
    print('取款成功,余额为', money)

# 双分支结构
'''
  if 条件表达式：
      条件执行体1
  else：
      条件执行体2
'''
print('-----判断键盘输入的整数是奇数还是偶数-----')
num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')



