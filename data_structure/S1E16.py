"""

测试题：
   
0. 我们根据列表、元组和字符串的共同特点，把它们三统称为什么？

序列

1. 请问分别使用什么BIF，可以把一个可迭代对象转换为列表、元组和字符串？
   
list()
tuple()
str()

2. 你还能复述出“迭代”的概念吗？
  
逐个取出元素的操作

3. 你认为调用 max('I love FishC.com') 会返回什么值？为什么？

v,在ASCII码中，小写的值比大写的大

4. 哎呀呀，现在的小屁孩太调皮了，邻居家的孩子淘气，把小甲鱼刚写好的代码
画了个图案，麻烦各位鱼油恢复下代码~~

"""
name = input("请输入待查找的用户名：")
score = [['迷途',85],['黑夜',80],['小布丁',65],['福禄娃娃',95],['怡静',90]]
IsFind = False
for each in score:
    if name in each[0]:
        print(name + "的得分是:",each[1])
        IsFind = True
        break
if not IsFind:
    print("查找的数据不存在！")

"""
动动手：
   
0. 猜想一下 min() 这个BIF的实现过程
   
"""
str1 = [1,2,3,4,5,6,7,-12,8,9,11,32]
Min_num1 = min(str1)

Min_num2 = str1[0]
for i in str1:
    if i < Min_num2:
        Min_num2 = i
print(f"Min_num1 = {Min_num1}\nMin_num2 = {Min_num2}")
"""
1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话
就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确
的计算结果
   
"""
str2 = [1,2,'hello world',3,4,'嘿嘿'\
        ,5,6,7,-12,'此处的作用是作为字符串',8,9,11,32]
Num_sum = 0
for each in str2:
    if isinstance(each,int):
        Num_sum += each
print(f"Num_sum = {Num_sum}")

try:
    print(f"Num_sum = {sum(str2)}")
except TypeError as e:
    print(f"Num_sum = sum(str2)无法获得结果\n找到错误：{e}")
#  2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
