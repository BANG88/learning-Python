def main():
	n = int(input("Enter a number: "))
	for i in sheep(n):
		print(i)


def sheep(n):
	for i in range(n):
		yield ("🐏" * i)



if __name__ == '__main__':
	main()