"""
mario
Created at: 2024/1/17 by bang
"""

def main():
   print_square(3)

   x =  get_int()
   print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


def print_square(n):
    for i in range(n):
        for j in range(n):
            print('#', end='')
        print()


def print_row(n):
    print('?' * n, end='')

def print_column(n):
    for i in range(n):
        print('#')






main()