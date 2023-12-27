"""
example07
Created at: 2023/12/26 by bang
"""

# 五人分鱼

fish = 1
while True:
    total, enough = fish, True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 1
