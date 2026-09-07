from typing import Tuple
def get_int(x:str) -> int:
    try:
        return int(input(x))
    except Exception as E:
        print(f"错误原因：{E}\n并且默认返回了'0'")
        return 0


def get_two_int(str1:str = '请输入两个整数，用空格隔开：') -> Tuple[int,int]:
    try:
        str1 = input(str1).strip().split()
        x,y = int(str1[0]),int(str1[1])
        return x,y
    except Exception as E:
        print(f"错误原因：{E}\n默认返回1，2")
        return 1,2


"""1.正负零判断
输入一个整数，输出它是正数、负数还是零。
"""
num = get_int("0.正负零判断,请输入一个整数:")
if num > 0:
    print("正整数")
elif num < 0:
    print("负整数")
else:
    print("0")

    
"""
2.闰年判断
输入一个年份，判断是否为闰年（规则：能被4整除但不能被100整除，或者能被400整除）。
"""
year = get_int("1.闰年判断,请输入年份：")
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("闰年")
else:
    print("平年")

    
"""
3.三个数求最大
输入三个数，输出其中的最大值（不使用内置max()函数）。
"""
try:
    a , b, c = map(int, input("2.三个数求最大,请输入三个数，并使用空格分开：").split())
    print(f"最大值{a if a > b and a > c else b if b > c else c}")
except ValueError as E:
    print(f"错误原因：{E}")


"""
4.成绩等级划分
输入百分制成绩（0~100），按以下规则输出等级：

90~100 → A

80~89 → B

70~79 → C

60~69 → D

<60 → F
若输入超出范围，提示“无效成绩”。(提示：在正常情况下，60~79的人数较多，可以考虑提高效率的方法)
"""

score = get_int("3.成绩等级划分,请输入成绩：")
if 60 <= score < 70:
    print("D")
elif 70 <= score < 80:
    print("C")
elif 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif score < 0 or score > 100:
    print("成绩异常！")
else:
    print("F")


"""
5.素数判断
输入一个正整数，判断它是否为素数（只能被1和自身整除）。
"""
def s_nums(x):
    if x <= 1:
        print("否")
    elif x <= 3:
        print("是")
    elif x % 2 == 0:
        print("否")
    else:
        is_s = 0
        for i in range(3,x // 2 + 2,2):
            if x % i == 0:
                print("否");break
            else:
                is_s = 1
        if is_s:
            print("是")
n = get_int('4.素数判断:')
s_nums(n)


"""
6.打印1~100的奇数
使用for循环打印1到100之间所有的奇数。
"""
list1 = [i for i in range(1,100,2)]
print("5.打印0-100的奇数",end = '')
print(list1)


"""
7.求1~100的偶数和
计算并输出1到100之间所有偶数的和。
"""
list2 = [i for i in range(2,101,2)]
print("6.打印0-100的奇数和以及偶数和",end = '')
print(sum(list2))
print(sum(list1))


"""
8.斐波那契数列
输入项数n，输出斐波那契数列的前n项（从0、1开始）。
"""
list1 = [0,1]
n = get_int("7.斐波那契数列,输入项数n：")
if n == 0:
    print("无")
elif n == 1:
    print([0])
else:
    for i in range(n-2):
        list1.append(list1[i] + list1[i+1])
    list2 = [(x,n) for x,n in zip(list1,range(1,n+1))]
    print(*list2,sep = '\n')


"""
9.阶乘计算
输入非负整数n，计算n!（0! = 1）。
"""
n = get_int("8.阶乘计算，输入非负整数：")
count = 1
if n == 0:
    print("1")
else:
    for i in range(1,n+1):
        count *= i
    print(count)


"""
10.回文字符串判断
输入一个字符串，判断它是否回文（忽略大小写，如 "Radar" 视为回文）。
"""
try:
    str1 = input("9.回文字符串判断，输入一串字符串：").lower()
    if str1 == str1[::-1]:
        print("是")
    else:
        print("否")
except Exception as E:
    print(f"错误原因：{E}")


try:
    str1 = input("9.1.输入一串字符串：").lower()
    if str1 == "".join(reversed(str1)):
        print("是")
    else:
        print("否")
except Exception as E:
    print(f"错误原因：{E}")


"""
11.最大公约数（GCD）
输入两个正整数，使用辗转相除法求它们的最大公约数。
"""
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x
x,y = get_two_int("10.最大公约数（GCD），输入两个整数，用空格隔开：")
print(gcd(x,y))

"""
12.最小公倍数（LCM）
输入两个正整数，输出它们的最小公倍数（可利用GCD）。
"""
x,y = get_two_int("11.最小公倍数（LCM），请输入两个整数，用空格隔开：")
print(x // gcd(x,y) * y)


"""
13.打印九九乘法表
使用嵌套循环输出九九乘法表（格式整齐）。
"""
print("12.打印乘法表：")    #上三角
for i in range(1,10):
    for j in range(i,10):
        print(f"{i} * {j} == {i*j:2d}  ",end = '')
    print('\n')


"""
14.打印金字塔（*）
输入行数n，打印由*组成的等腰三角形金字塔。
"""
def print_star():
    n = get_int("13.打印（*），请输入行数:")
    for i in range(1,n+1):
        print(" " * (n - i),end = '')
        for j in range(2 * i - 1):
            print("*",end = '')
        print(" " * (n - i),end = '')
        print()
print_star()


"""
15.打印菱形图案
输入奇数n，打印由*构成的菱形（如n=5时，上下对称）。
"""
n = get_int("14.请输入奇数行数：")
if n % 2 == 0:
    print("请输入奇数")
else:
    for i in range(1, n//2 + 2):
        print(" " * (n - i) + "*" * (2*i - 1))
    for i in range(n//2, 0, -1):
        print(" " * (n - i) + "*" * (2*i - 1))


"""
16.循环输入求平均值
使用while循环不断输入数字，直到输入0为止，计算所有非零输入的平均值。
"""
num = get_int("15.循环输入数字求平均值，输入为0时停止：")
sum_nums = 0
count = 0
while num:
    count += 1    #数字的个数
    sum_nums += num    #总数
    num = get_int("")
if count == 0:
    print("无有效数字")
else:
    print(sum_nums / count)


"""
17.遍历列表打印索引和值
给定列表lst = ['a', 'b', 'c', 'd']，使用for循环打印每个元素的索引和值。
"""
lst = ['a','b','c','d']
print('18.',end='')
index = 0
for i in lst:
    print(index,end='');index += 1;print(f'{i:2}',end='')
print()


"""
18.break查找第一个大于100的数
在列表[45, 78, 120, 56, 200]中，用循环找到第一个大于100的数并打印，
若没有则输出"未找到"。
"""
nums = [45,78,120,56,200]
str1 = []
count = 0
for i in nums:
    if i > 100:
        str1.append(i);count += 1
if count:
    print(f'17.{str1[0]}')
else:
    print("17.没找到")

nums = [45,78,120,56,200]
str1 = []
count = 0
for i in nums:
    if i > 100:
        print(f'17.{i}');break
    else:
        print("17.没找到")
"""
19.continue跳过3的倍数
使用循环打印1~20中所有不能被3整除的数。
"""
print("18.")
for i in range(1,21):
    if i % 3 != 0:
        print(f"{i:3d}",end='')
    else:
        continue
print()


"""
20.完全数寻找
输入正整数n，打印所有小于n的完全数（完全数等于其真因子之和，如6=1+2+3）。
"""
n = get_int("19.输入正整数：")
for i in range(1,n):
    nums = []
    for j in range(1,i):
        if i % j == 0:
            nums.append(j)
    if int(sum(nums)) == i:
        print(i)


"""
21.字符频次统计
输入一个字符串，统计其中每个字符出现的次数（使用字典存储结果）。
"""
def char_frequency(s: str) -> dict:
    """
    统计字符串中每个字符出现的次数。
    
    参数:
        s: 输入字符串
        
    返回:
        字典，键为字符，值为出现次数
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 示例
if __name__ == "__main__":
    text = input("请输入一个字符串: ")
    result = char_frequency(text)
    print("字符频次统计结果:")
    for char, count in result.items():
        print(f"'{char}': {count}")



"""
22.列表去重
输入一个列表（如[1,2,2,3,3,3,4]），输出去重后的新列表（保持原有顺序）。
"""
text = input("21.输入多个元素并使用','隔开：")
str1 = text.split(',')
new_str = []
for ch in str1:
    if ch not in new_str:
        new_str.append(ch)
print(new_str)


"""
23.数字反转
输入一个正整数，将其各位数字反转后输出（如1234 → 4321）。
"""
n = get_int("22.输入一个正整数：")
reversed_n = int(str(n)[::-1])
print(reversed_n)


"""
24.阿姆斯特朗数判断
输入一个三位数，判断它是否为阿姆斯特朗数（水仙花数，
即各位数字立方和等于自身，如153）。
"""
while True:
    n = get_int("23.输入一个三位数：")
    if 100 <= n <= 999:
        if n == sum(int(num) ** 3 for num in str(n)):
            print("是")
        else:
            print("否")
        break
    else:
        print("请输入三位数，而不是二位数")


"""
25.简易计算器.
输入两个数字和一个运算符（+、-、*、/），输出运算结果，若除数为0则提示“除数不能为0”。
"""
try:
    a, b = get_two_int("24.输入两个数字，用空格隔开：")
    op = input("输入运算符（+、-、*、/）：").strip()
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b == 0:
            print("除数不能为0")
        else:
            print(a / b)
    else:
        print("不支持的运算符")
except Exception as e:
    print("输入错误：", e)


"""
26.十进制转二进制
输入一个正整数，输出其二进制表示（不使用bin()函数，手动实现）。
"""
n = get_int("25.请输入一个正整数：")
if n == 0:
    print("0b0")
else:
    orginal_n = n ; nums = []
    while n:
        nums.append(str(n % 2))
        n //= 2
    nums.reverse()
    bin_n = ''.join(nums)
    print(f"0b{bin_n}")
    print(bin(orginal_n))


"""
27.十进制转八进制和十六进制
输入一个正整数，分别输出它的八进制和十六进制表示（可使用内置函数oct()和hex()）。
"""
n = get_int("26.输入一个正整数：")
print(oct(n));print(hex(n))


"""
28.打印所有三位水仙花数
找出并打印所有三位阿姆斯特朗数（水仙花数）。
"""
print("27.打印所有三位水仙花数")
for i in range(100,1000):
    sum_nums = sum(int(num)**3 for num in str(i))
    if sum_nums == i:
        print(i)


"""
29.等腰三角形（递增星号）
输入行数n，打印一个每行星号数量递增的等腰三角形
（如n=5时第一行1个，第二行2个……）。
"""
n = get_int("28.打印（*），请输入行数:")
for i in range(1,n+1):
    print(" " * (n - i) + "* " * i)
    print()



"""
30.输出1~n之间的所有素数
输入正整数n，输出从2到n之间的所有素数，每行一个。
"""
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for d in range(3, int(x ** 0.5) + 1, 2):
        if x % d == 0:
            return False
    return True

n = get_int("29.输入正整数n，将输出1~n之间的所有素数:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i)

