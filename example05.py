"""
example05
Created at: 2023/12/26 by bang
"""

# 输入一个正整数n，将n反转后输出

n = int(input("请输入一个正整数："))
m = 0
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
print(m)

# 打印1~100之间的所有质数
# 质数：只能被1和自身整除的数

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
print()

# 数字矩阵

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
    print()

n = int(input("请输入一个正整数："))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()
