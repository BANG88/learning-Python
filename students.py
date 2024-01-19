import csv

name = input("Enter your name: ")
house = input("Enter your house: ")
city = input("Enter your city: ")

try:
	with open("students.csv",'a') as file:
		writer = csv.DictWriter(file, fieldnames=["name", "house", "city"])
		writer.writerow({
			"name": name,
			"house": house,
			"city": city
		})
except Exception as e:
	print("An error occurred while writing to the file:", str(e))

# name,house,city
	

