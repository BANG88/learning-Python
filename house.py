"""
house
Created at: 2024/1/16 by bang
"""

name = input("What is your name? ")


match name:
    case "bang" | "Bang" | "BANG":
        print("Hello, bang!")
    case "tony":
        print("Hello, tony!")
    case _:
        print("Hello, stranger!")
