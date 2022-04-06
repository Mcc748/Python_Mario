# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/2 15:05

# 嵌套if的语法结构
'''
  if 条件表达式1：
     if 内层条件表达式：
        内层条件执行体1
     else：
        内层条件执行体2
  else:
    条件执行语句N
'''
'''
案例1：
         会员 >= 200 8折
             >= 100 9折
                不打折
         非会员 >= 200 9.5折
                不打折
'''
c = input('您是会员吗？Y/N')
money = float(input('请输入您的购物金额：'))
if c == 'y':  # 会员
    if money >= 200:
        print('八折优惠,您的付款的金额为：', money * 0.8)
    elif money >= 100:
        print('九折优惠,您的付款的金额为：', money * 0.9)
    else:
        print('金额低于100没有折扣，您的付款金为：', money)
else:
    if money >= 200:
        print('九五折优惠,您的付款金额为：', money * 0.95)
    else:
        print('金额低于200没有折扣,您的付款金额为：', money)
