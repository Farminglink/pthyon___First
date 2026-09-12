
while True:
    temp = input("请输入一个整数(输入Q结束程序)：")

    if temp.upper() == 'Q':
        print("结束程序")
        break
    
    convert = int(temp)
    print("十进制 -> 十六进制：{0} -> {0:#x}".format(convert))
    print("十进制 -> 八进制：%d -> %#o" % (convert,convert))
    print(f"十进制 -> 二进制：{convert} -> {bin(convert)}")
