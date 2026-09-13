"""
0. 你有听说过DRY吗？

DAR，不要让重复的代码反复出现，使用函数封装解决

1. 都是重复一段代码，为什么我要使用函数（而不使用简单的拷贝黏贴）呢？  

简单拷贝容易导致可读性变差，程序代码维护难得升高

2. 函数可以有多个参数吗？

可以

3. 创建函数使用什么关键字，要注意什么？

def ，还要有()

4. 请问这个函数有多少个参数？
def MyFun((x, y), (a, b)):
    return x * y - a * b

两个

5. 请问调用以下这个函数会打印什么内容？
def hello():
    print('Hello World!')
    return
    print('Welcome To FishC.com!')

Hello World!

"""

"""
动动手：

0. 编写一个函数 power() 模拟内建函数 pow()，即 power(x, y) 为计算
并返回 x 的 y 次幂的值。

"""
print("0.")
def power(x,y):
    return x ** y
print(power(2,4))
print(pow(2,4))

print("\n\n\n\n\n\n")

"""

1. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，
例如 gcd(x, y) 返回值为参数 x 和参数 y 的最大公约数。

"""
print("1.")
def gcd(x,y):
    while y:
        x,y = y,x % y
    return x
print(gcd(12,18))

print("\n\n\n\n\n\n")

"""

2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（补脑链接）的方式，结果与调用 bin() 一样返回字符串形式。

"""
def b_convert(x):
    if x == 0:
        return '0'

    count = []
    while x > 0:
        temp = x % 2
        count.append(str(temp))
        x = x // 2

    return "0b" + "".join(count[::-1])
print(b_convert(10))
print(bin(10))
"""

3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

"""
