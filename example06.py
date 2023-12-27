"""
example06
Created at: 2023/12/26 by bang
"""

# 计算 三角形的周长和面积

while True:
    a = float(input("请输入三角形的第一条边的长度："))
    b = float(input("请输入三角形的第二条边的长度："))
    c = float(input("请输入三角形的第三条边的长度："))
    if a + b > c and a + c > b and b + c > a:
        print("三角形的周长为：", a + b + c)
        p = (a + b + c) / 2
        print("三角形的面积为：", (p * (p - a) * (p - b) * (p - c)) ** 0.5)
        break
    else:
        print("您输入的三条边不能构成三角形，请重新输入！")

# 计算圆的周长和面积

while True:
    r = float(input("请输入圆的半径："))
    if r > 0:
        print("圆的周长为：", 2 * 3.14 * r)
        print("圆的面积为：", 3.14 * r**2)
        break
    else:
        print("您输入的半径不合法，请重新输入！")

# 计算矩形的周长和面积

while True:
    width = float(input("请输入矩形的宽度："))
    height = float(input("请输入矩形的高度："))
    if width > 0 and height > 0:
        print("矩形的周长为：", 2 * (width + height))
        print("矩形的面积为：", width * height)
        break
    else:
        print("您输入的宽度或高度不合法，请重新输入！")
