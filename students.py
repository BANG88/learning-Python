import csv

students = []

with open("students.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		students.append(row)


for student in sorted(students, key=lambda student: student["city"]):
	print(f"{student['name']} is in {student['house']} house and is from {student['city']}")



