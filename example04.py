"""
example04
Created at: 2023/12/26 by bang
"""
import time
import math

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()


for i in range(1, 101, 6):
    print(f"{i} * {i} = {i * i}")

# 实现1~100求和的效果
total = 0
for x in range(101):
    total += x
    print(f"当前的x值为{x}, 当前的total值为{total}")
print(total)

# 实现1~100之间偶数求和的效果
total = 0
for x in range(2, 101, 2):
    total += x
    print(f"当前的x值为{x}, 当前的total值为{total}")
print(total)

# 实现1~100之间奇数求和的效果
total = 0
for x in range(1, 101, 2):
    total += x
    print(f"当前的x值为{x}, 当前的total值为{total}")
print(total)

# while循环
i = 0
while i < 100:
    print(i)
    i += 1
print("while循环结束")

# sum 1~100

print(f"sum 1~100: {sum(range(1, 101))}")


# 找出1~9999之间的所有完美数


start = time.time()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num // factor != factor:
                sum += num // factor
    if sum == num:
        print(num)
end = time.time()
print(f"执行时间: {end - start}秒")


# 输入两个正整数计算最大公约数和最小公倍数
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f"最大公约数为{factor}")
        print(f"最小公倍数为{x * y // factor}")
        break

# 打印三角形图案
row = int(input("请输入行数: "))
for i in range(row):
    for _ in range(i + 1):
        print("*", end="")
    print()
