class Cat:
	MEOWS = 3

	def meow(self):
		for _ in range(self.MEOWS):
			print("meow")



def main():
	cat = Cat()
	cat.meow()
	


if __name__ == '__main__':
	main()

