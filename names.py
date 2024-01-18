names = []

# for _ in range(3):
# 	names.append(input("Enter a name: "))

# for name in sorted(names):
# 	print(f"Hello {name}!")


# with open("names.txt", "a") as file:
# 	file.write(str(names))



with open("names.txt", "r") as file:
	lines = file.readlines()
	for l in file:
		names.append(l.strip())

print(names)

for l in lines:
	print(l.strip())


