def meow(n:int) -> str:
	"""
	Meow n times

	:param n: number of meows
	:type n: int
	:rises: ValueError if n is negative
	:returns: a string of n meows separated by newlines
	:rtype: str
	"""
	return "meow \n" * n




number:int  = int(input("How many times do you want to meow? "))

meow(number)

meows: str = meow(number)

print(meows)