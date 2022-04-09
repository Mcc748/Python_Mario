# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/4/9 15:48

'''
     break语句:用于结束循环语句,通常和分支结构if一起使用
'''

# 1> ATM取款,三次输入密码错误自动退卡
''' 方法1:使用for循环
password = 258011
for tice in range(3):
    ac = int(input('请输入6位银行卡密码：'))
    if ac == password:
         print('密码验证成功')
         break
    else:
         if tice == 0:
            print('第一次密码输入错误,请重新输入')
         elif tice == 1:
            print('第二次密码输入错误,请重新输入')
         else:
            print('三次密码输入错误,卡已退出')  '''

# 方法2:使用while循环
password = 258011
a = 0
while a<3:
    psin = int(input('请输入6位银行卡密码：'))
    a += 1
    if psin == password:
        print('密码验证成功')
        break
    else:
        if a == 1:
            print('第一次密码输入错误,请重新输入')
        elif a == 2:
            print('第二次密码输入错误,请重新输入')
        else:
            print('三次密码输入错误,卡已退出')










