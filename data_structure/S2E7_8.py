score = int(input("请输入0-100的成绩："))
if 60 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif score < 60:
    print("D")
elif score >= 90:
    print("A")
else:
    print("错误成绩")

'''修改为三元操作符实现'''

x,y,z = 6,5,4
if z < x < y:
    small = z
elif y < z:
    small = y
else:
    small = z
print(f"{small}是最小值")
