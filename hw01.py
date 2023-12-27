"""
hw01
Created at: 2023/12/26 by bang
"""

# 猜数字游戏
import random

# 生成随机数
num = random.randint(1, 100)
# print(num)

# 猜数字
# while True:
#     guess = int(input("请输入你猜的数字："))
#     if guess > num:
#         print("猜大了")
#     elif guess < num:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break

# 猜数字游戏升级版

# 生成随机数
num = random.randint(1, 100)
# print(num)

# 猜数字
count = 0
while True:
    guess = int(input("请输入你猜的数字："))
    if guess > num:
        print("猜大了")
        count += 1
    elif guess < num:
        print("猜小了")
        count += 1
    else:
        print("猜对了")
        count += 1
        break
    if count == 7:
        print("你已经猜了7次了，游戏结束")
        break
