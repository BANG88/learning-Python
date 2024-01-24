def meow(n:int) -> str:
	return "meow \n" * n




number:int  = int(input("How many times do you want to meow? "))

meow(number)

meows: str = meow(number)

print(meows)