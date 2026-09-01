# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：
#~!@#%^&*()_=-/,.?<>;:[]{}|\）任意两种组合 
#   2. 密码长度不能低于8位 
# 
# 高级密码要求： 
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
import re

symbols = r"""~!@#%^&*()_=-/,.?<>;:[]{}|\\"""   #symbols,允许使用的特殊字符

password = input("请输入需要检测的密码组合：")

has_alpha = any(c.isalpha() for c in password)
has_lower = any(c.islower() for c in password)    #检验小写
has_upper = any(c.isupper() for c in password)    #检验大写
has_renum = bool(re.search(r'\d{3,}',password))         #检验数字是否连续
has_realp = bool(re.search(r'[a-zA-Z]{3,}',password))   #检验字母是否连续
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in symbols for c in password)    #检验是否存在特殊符合

sum_safty = sum([has_alpha,has_digit,has_symbol])   #计算三者是否同时存在与否

if sum_safty == 3 and password[0].isalpha() and len(password) > 16:
    temp = '高'
elif sum_safty >= 2 and len(password) > 8:
    temp = '中'
else:
    temp = '低'

if temp == '低':
    print("""您的密码安全级别判定为：低
请按照一下方式提升您的密码安全级别：
        1.密码必须由数字、字母及特殊字符三种组合
        2.密码只能由字母开头
        3.密码长度不能低于16位""")
elif temp == '中':
    print("""您的密码安全级别判定为：中
请按照一下方式提升您的密码安全级别：
        1.密码必须由数字、字母及特殊字符三种组合
        2.密码只能由字母开头
        3.密码长度不能低于16位""")
else:
    print("""您的密码安全级别判定为：高
请继续保持""")


tips = []

if has_lower and not has_upper:
    tips.append('请适当使用大写字母增加安全性')
elif not has_lower and has_upper:
    tips.append('请适当使用小写字母增加安全性')
    
if not has_renum:
    tips.append('请减少连续数字的使用增加安全性')
elif not has_realp:
    tips.append('请减少连续字母的使用增加安全性')

if tips:
    for tip in tips:
        print(f'{tip}')
