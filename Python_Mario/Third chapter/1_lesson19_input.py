# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/30 13:44

# Python的输入函数input（）

'''
            ①、作用：接收来自用户的输入
input函数：  ②、返回值类型：输入值的类型为str
            ③、值的存储：使用=对输入的值进行存储
'''

present = input('猴哥想要什么礼物呢？')
print(present, type(present))  # 在运行窗口问号后面输入'棒子',然后回车就得到了用户的输入数据

a = input('输入第一个整数')
b = input('输入第二个整数')
print(type(a), type(b))
# print(int(a)+int(b)) # 第一种方法：直接在输出里面转换类型
a = int(a)    # 第二种方法：先转换字符类型
b = int(b)    # 第二种方法
print(a+b)    # 第二种方法

'''
第三中方法：直接在输入的时候就进行转换类型
a = int(input('输入第一个整数'))
b = int(input('输入第二个整数'))
print(a+b)
'''












