"""
0. 请问以下哪个是形参哪个是实参？
def MyFun(x):
    return x ** 3

y = 3
print(MyFun(y))

x为形参，y为实参

1. 函数文档和直接用“#”为函数写注释有什么不同？

可以被使用__doc__输出
     
2. 使用关键字参数，可以有效避免什么问题的出现呢？

多个参数输入错误
     
3. 使用 help(print) 查看 print() 这个 BIF 有哪些默认参数？分别起到什么作用？

*args 是读取列表录入多个元素；sep=' ' 是多个元素间的间隔用空格分开；
end='\n' 是用换行符结尾；file=none默认把文件输出到终端；
flush='False' 不知道
     
4. 默认参数和关键字参数表面最大的区别是什么？

在不输入时，默认参数也能运行                             

"""
"""
动动手：
     
0. 编写一个符合以下要求的函数：
   
计算打印所有参数的和乘以基数（base=3）的结果（比如 mFun(1, 2, 3, 4, 5) 的
结果为 45）如果参数中最后一个参数为（base=5），则设定基数为 5，基数不参与
计算（比如 mFun(1, 2, 3, 4, 5, base=5) 的结果为 75）。
"""
def SumandCount(*nums,base):
    """计算参数之和和基数的乘积"""
    return sum(nums) * base

print(SumandCount(1,2,3,4,5,base=5))
"""   
1. 寻找水仙花数
   
题目要求：如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。

例如 153 = 1^3+5^3+3^3，因此 153 是一个水仙花数。编写一个程序，找出所有
的水仙花数。
"""
def Nar_num():
    """水仙花数计算"""
    for i in range(100,1000):
        sum_nums = sum(int(num) ** 3 for num in str(i))
        if sum_nums == i:
            print(i)
print(Nar_num())
"""      
2. 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个
字符串中出现的次数。例如：假定输入的字符串为 “You cannot improve your
past, but you can improve your future. Once time is wasted, life is wasted.”
，子字符串为 “im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。
     
程序执行效果：
"""
def findstr(main_str,son_str):
    """查找子字符串"""
    count,start = 0,0
    while True:
        index = main_str.find(son_str,start)
        if index == -1:
            break
        count += 1
        start = index + 1
    if count:
        print(f"子字母串在目标字符串中共出现 {count} 次")
    else:
        print("无")
print(findstr("You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.",'im'))
"""   
3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

"""
