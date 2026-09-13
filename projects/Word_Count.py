str1 = input("输入待统计的字符串：")

new_file = []
file_count = []

for ch in str1:
    if ch not in new_file:
        new_file.append(ch)
        file_count.append(1)
    else:
        index = new_file.index(ch)
        file_count[index] += 1
result = [(ch,num) for ch,num in zip(new_file,file_count)]
print(result)
