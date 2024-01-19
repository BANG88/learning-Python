import csv

students = []

with open("students.csv") as file:
	for line in file:
		name, house, city = line.rstrip().split(",")
		student = {
			"name": name,
			"house": house,
			"city": city
		}
		students.append(student)


for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is in {student['house']} house and is from {student['city']}")

