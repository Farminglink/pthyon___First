"""
0. 使用递归编写一个十进制转换为二进制的函数
（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）。
"""
def local_bin(n):
    nums = []
    
    if n == 0:
        return '0b0'
    
    if n < 0:
        sign = '-'
        n = abs(n)
    else:
        sign = ''
        
    def in_bin(x):
        if x == 0:
            return ''
        return in_bin(x//2) + str(x % 2)
    return sign + '0b' + in_bin(n)

n = int(input())

print(local_bin(n))
print(bin(n))
"""
1. 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
举例：get_digits(12345) ==> [1, 2, 3, 4, 5]
"""
num = int(input())

def get_digits_1(n):
    """迭代"""
    length = len(str(n))
    nums = []
    for _ in range(length):
        nums.append(int(n) % 10)
        n = n // 10
    return nums
print(list(get_digits_1(num)))


def get_digits_2(n):
    """递归"""
    if n == 0:
        return '0'
    def in_digits(x):
        if x  == 0:
            return ''
        return str(x % 10) + in_digits(x//10)
    return list(in_digits(num))
    
nums = get_digits_2(num)
nums = list(map(int,nums))

print(nums)
"""
2. 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，
亲还能骄傲的说我可以吗？
"""
def ispanlindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return ispanlindrome(s[1:-1])
s = input()
print(ispanlindrome(s))
"""
3. 使用递归编程求解以下问题：

有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
"""
def count_age(n):
    if n == 0:
        return 10
    return count_age(n-1) + 2
age = int(input())
print(count_age(age))
