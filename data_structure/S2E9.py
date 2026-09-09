'''设计一个验证用户密码程序，用户只有三次机会输入错误，不
过如果用户输入的内容中包含"*"则不计算在内'''

password = "123456"
chance = 3
while chance > 0:
    user_input = input("请输入正确密码：")

    if '*' in user_input:
        print("密码中不能含有*号，请重新输入密码：")
        continue

    if user_input == password:
        print("密码正确")
        break
    else:
        chance -= 1
        if chance > 0:
            print(f"密码错误，还有{chance}次机会")
        else:
            print("次数用尽")
            break

'''编写一个程序，求 100~999 之间的所有水仙花数。如果一个
3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：
153 = 1^3 + 5^3 + 3^3，因此 153就是一个水仙花数。'''

for i in range(100,1000):
    if (i // 100) ** 3 + ((i % 100) // 10) ** 3 + (i % 10) ** 3 == i:
        print(i)
    else:
        continue

'''三色球问题有红、黄、蓝三种颜色的球，其中红球 3 个，黄球
3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任
意摸出 8 个球，编程计算摸出球的各种颜色搭配。'''

print("红球\t黄球\t绿球")
count = 0

for r in range(0, 4):
    for y in range(0, 4):  
        g = 8 - r - y
        if 0 <= g <= 6:
            print(f"{r}\t{y}\t{g}")
            count += 1

print(f"\n共有 {count} 种搭配")
