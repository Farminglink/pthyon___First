"""
0. 下边程序会输入什么？
def next():
    print('我在next()函数里...')
    pre()

def pre():
    print('我在pre()函数里...')
   
next()

我在next()函数里...
我在pre()函数里...


1. 请问以下这个函数有返回值吗？
def hello():
        print('Hello FishC!')

None


2. 请问 Python 的 return 语句可以返回多个不同类型的值吗？

可以


3. 目测以下程序会打印什么内容:
def fun(var):
    var = 1314
    print(var, end='')

var = 520
fun(var)
print(var)

1314520


4. 目测以下程序会打印什么内容？
var = ' Hi '

def fun1():
    global var
    var = ' Baby '
    return fun2(var)

def fun2(var):
    var += 'I love you'
    fun3(var)
    return var

def fun3(var):
    var = ' 小甲鱼 '

print(fun1())

 Baby I love you
                           

动动手：版权属于：
0. 编写一个函数，判断传入的字符串参数是否为“回文联”
（回文联即用回文形式写成的对联，既可顺读，也可倒读。
例如：上海自来水来自海上）
"""
def function1(str1):
    if str1 == str1[::-1]:
        print("是")
    else:
        print("否")

str1 = input("输入字符串：")
function1(str1)

"""
1. 编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的
英文字母、空格、数字和其它字符的个数。
程序执行结果如图：
"""
def count(*strings):
    for idx, s in enumerate(strings, 1):
        letters = digits = spaces = others = 0
        for ch in s:
            if ch.isalpha():      
                letters += 1
            elif ch.isdigit():     
                digits += 1
            elif ch.isspace():     
                spaces += 1
            else:
                others += 1       
        print(f"第 {idx} 个字符串共有：英文字母 {letters} 个，\
              数字 {digits} 个，空格 {spaces} 个，其他字符 {others} 个。")
"""
2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
"""
