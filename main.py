print("hello", end=" ### ")
print("world")

"""
hello
world
"""


"""
变量命名需注意

- 字母、数字、下划线，不能使用特殊字符，不能数字开头
- Unicode 字符也可以
- 区分大小写
- 不能使用Python的关键字和保留字
- 不能使用内置函数名
- 不能使用自定义函数名
- 不能使用模块名
- 不能使用自定义模块名
- 命名规范：见名知意，驼峰命名法 myNameIs 、下划线命名法 my_name_is、 帕斯卡命名法 MyNameIs
- 常量：全部大写，多个单词用下划线连接 MY_NAME_IS
- 变量：全部小写，多个单词用下划线连接 my_name_is
- 类：帕斯卡命名法 MyNameIs
- 函数：下划线命名法 my_name_is
- 模块：下划线命名法 my_name_is
- 包：下划线命名法 my_name_is
- 模块内部的私有变量：下划线开头 _my_name_is
- 模块内部的私有函数：下划线开头 _my_name_is
- 模块内部的私有类：下划线开头 _MyNameIs
- 模块内部的私有包：下划线开头 _my_name_is


"""


a = int(input("请输入一个数字："))
b = int(input("请输入另一个数字："))


print(100 % 3)
# 整除法，结果没有小数
print(a // b)
print(a / b)

name = "邦"

print("姓名： %s" % name)
print("%d + %d = %d" % (a, b, a + b))

print(f"{a} + {b} = {a+b}")
