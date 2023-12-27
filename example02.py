"""
example02
Created at: 2023/12/25 by bang
"""


import math

radius = float(input("请输入圆的半径: "))

perimeter = 2 * math.pi * radius

print(perimeter)

area = math.pi * radius * radius

print(f"圆的周长为: {perimeter:.2f}")
print(f"圆的面积为: {area:.2f}")

print("圆的周长为: %.2f" % perimeter)
