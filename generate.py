"""
generate
Created at: 2024/1/18 by bang
"""

from random import choice,randint, shuffle

coin = choice(['heads', 'tails'])

print(coin)

print(randint(1, 6))



# shuffle
players = ['charles', 'martina', 'michael', 'florence', 'eli']
shuffle(players)
print(players)


for i in range(10):
    print(randint(1, 6))