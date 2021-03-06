# Name : Mario Zeng
# Email: z462949992@gmail.com
# Time : 2022/3/30 20:46

# 位运算符：将数据转换成二进制进行计算
'''
         1>  位与 ---> & ---> 对应数位都是1,结果数位才是1,否者为0
         2>  位或 ---> | ---> 对应数位都是0,结果数位才是0,否则为1
位运算符  3>   左移位运算符 ---> << ---> 高位溢出舍弃,低位补0
         4>   右移位运算符 ---> >> --->低位溢出舍弃,高位补0
'''

print(4 & 8)  # 结果为0, 因为需要先将4和8转换为二进制数再以位进行与计算

print(4 | 8)  # 结果为12, 因为需要先将4和8转换为二进制数再以位进行与计算

print(4 << 1)  # 结果为8
print(4 << 2)  # 结果为16
print(8 >> 1)  # 结果为4
print(8 >> 2)  # 结果为2






