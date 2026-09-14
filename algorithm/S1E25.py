"""
测试题：

0. 当你听到小伙伴们在谈论“映射”、“哈希”、“散列”或者“关系数组”的时候，事实上他们就是在讨论什么呢？

字典
"""
"""
1. 尝试一下将数据（'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115）创建为一个字典并访问键 'C' 对应的值？
"""
dict1 = dict((('F',70),('C',67),('h',104),('i',105),('s',115)))
print(dict1['C'])
print("="*80)
"""
2. 用方括号（“[]”）括起来的数据我们叫列表，那么使用大括号（“{}”）括起来的数据我们就叫字典，对吗？

{}内为空时是空字典，但{}内的值没有key和value时就不是字典

"""
"""
3. 你如何理解有些东西字典做得到，但“万能的”列表却难以实现（臣妾做不到T_T）？

快速查找某个值时，若索引为非整数，列表内置的方法无法快速查找；
主要还有一下情况：
"""
dict2 = {i : i * 2 for i in range(100000)}
list1 = [(i,i*2) for i in range(100000)]
#两者查找9999的时间复杂度就完全不一样，一个是O(1)一个是O(n)
"""
4. 下边这些代码，他们都在执行一样的操作吗？你看得出差别吗？
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
复制代码
"""
a = dict(one=1,two=2,three=3)
#key必须使用合法标识符
b = {'one':1,'two':2,'three':3}
#最直观最标准写法
c = dict(zip(['one','two','three'],[1,2,3]))
#当有两个一样长度的列表时可以使用，否则会在最短列表的长度截断
d = dict([('two',2),('one',1),('three',3)])
#适合与数据库搭配使用
e = dict({'three':3,'one':1,'two':2})
#浅拷贝
"""
5. 如图，你可以推测出打了马赛克部分的代码吗？
https://xxx.ilovefishc.com/forum/201403/21/002915fqfg88phmimxwxx3.png
"""
import webbrowser
webbrowser.open("https://xxx.ilovefishc.com/forum/201403/21/002915fqfg88phmimxwxx3.png")

data = "1000,李明,男"
MyDict = {}

(MyDict['id'],MyDict['name'],MyDict['sex']) = data.split(',')

print("ID:    "+MyDict['id'])
print("Name:  "+MyDict['name'])
print("Sex:   "+MyDict['sex'])
print()
print("="*80)
"""
动动手：

0. 尝试利用字典的特性编写一个通讯录程序吧，功能如图：
https://xxx.ilovefishc.com/forum/201403/21/003109a474un0hb4caqqt4.png
"""

contacts = {}
while True:
    order = int(input("请输入相关指令代码："))
    if order == 1:
        print("|--- 您正在使用查询功能 ---|")
        
        temp_name = input("请输入联系人姓名：")
        if temp_name in contacts:
            print(temp_name+' '+contacts[temp_name])
        else:
            temp = input("未查找到该联系人，是否录入？（Yes/No）")
            if temp == 'Yes':
                temp_name = input("请输入联系人姓名：")
                temp_phone_number = input("请输入用户联系电话：")
                contacts[temp_name] = temp_phone_number
        print()
    elif order == 2:
        print("|--- 您正在使用插入功能 ---|")
        
        temp_name = input("请输入联系人姓名：")
        
        if temp_name in contacts:
            print("您输入的姓名在通讯录中已存在 -->>"+contacts[temp_name])
            temp = input("是否修改用户资料(Yes/No)：")
            if temp == 'Yes':
                temp_phone_number = input("请输入用户联系电话：")
                contacts[temp_name] = temp_phone_number
        else:
            temp_phone_number = input("请输入用户联系电话：")
            contacts[temp_name] = temp_phone_number

        print()
    elif order == 3:
        print("|--- 您正在使用删除功能 ---|")
        temp_name = input("请输入联系人姓名：")
        if temp_name in contacts:
            del contacts[temp_name]
        else:
            print("联系人不存在")

        print()
    elif order == 4:
        print("|--- 感谢使用本通讯录程序 ---|")
        break
    else:
        print("程序错误")
        print()
ebbrowser.open("https://xxx.ilovefishc.com/forum/201403/21/003109a474un0hb4caqqt4.png")

print("""
|--- 欢迎进入通讯录程序 ---|
|--- 1：查询联系人资料  ---|
|--- 2：插入新的联系人  ---|
|--- 3：删除已有联系人  ---|
|--- 4：退出通讯录程序  ---|
""")
print()

contacts = {}
while True:
    order = int(input("请输入相关指令代码："))
    if order == 1:
        print("|--- 您正在使用查询功能 ---|")
        
        temp_name = input("请输入联系人姓名：")
        if temp_name in contacts:
            print(temp_name+' '+contacts[temp_name])
        else:
            temp = input("未查找到该联系人，是否录入？（Yes/No）")
            if temp == 'Yes':
                temp_name = input("请输入联系人姓名：")
                temp_phone_number = input("请输入用户联系电话：")
                contacts[temp_name] = temp_phone_number
        print()
    elif order == 2:
        print("|--- 您正在使用插入功能 ---|")
        
        temp_name = input("请输入联系人姓名：")
        
        if temp_name in contacts:
            print("您输入的姓名在通讯录中已存在 -->>"+contacts[temp_name])
            temp = input("是否修改用户资料(Yes/No)：")
            if temp == 'Yes':
                temp_phone_number = input("请输入用户联系电话：")
                contacts[temp_name] = temp_phone_number
        else:
            temp_phone_number = input("请输入用户联系电话：")
            contacts[temp_name] = temp_phone_number

        print()
    elif order == 3:
        print("|--- 您正在使用删除功能 ---|")
        temp_name = input("请输入联系人姓名：")
        if temp_name in contacts:
            del contacts[temp_name]
        else:
            print("联系人不存在")

        print()
    elif order == 4:
        print("|--- 感谢使用本通讯录程序 ---|")
        break
    else:
        print("程序错误")
        print()
