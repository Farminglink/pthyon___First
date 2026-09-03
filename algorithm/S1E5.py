while True:
    temp = input("请输入年份：")
    if temp.isdigit():
        while True:
            Year = int(temp);gage = ''
            if Year % 400 == 0:
                print("是闰年");gage = input("重新运行：(N/Y)")
            else:
                if Year % 4 == 0 and Year % 100 != 0:
                    print("是闰年");gage = input("重新运行：(N/Y)")
                else:
                    print("是平年");gage = input("重新运行：(N/Y)")
            if gage == 'Y':
                print("--------少女祈祷中......--------")
                temp = input("请重新输入年份：")
            else:
                print("程序结束");break
    else:
        print("错误格式")
