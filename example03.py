"""
example03.py
Created at: 2023/12/26 by bang
"""
from getpass import getpass

username = input("请输入用户名: ")
password = getpass("请输入密码: ")

if username == "admin" and password == "123456":
    print("身份验证成功")
    print("欢迎光临")
    print("请点击以下链接进入系统")
else:
    print("身份验证失败")


x = float(input("请输入x: "))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print(f"f({x}) = {y}")
