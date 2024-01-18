"""
hello
Created at: 2024/1/15 by bang
"""


def main():
    name = input("What is your name? ")
    hello(name)
    x = int(input("Enter a number: "))
    if is_even(x):
        print(x, "is even")
    else:
        print(x, "is odd".capitalize())


def is_even(n):
    return n % 2 == 0


def hello(to):
    print("Hello, ", to)


main()
