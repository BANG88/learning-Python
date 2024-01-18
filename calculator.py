"""
calculator
Created at: 2024/1/15 by bang
"""


def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))


def square(n):
    return pow(n, 2)


if __name__ == '__main__':
    main()
