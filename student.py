class Student:
	def __init__(self, name, house):
		if not name:
			raise ValueError("Name is required")
		if not house:
			raise ValueError("House is required")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is invalid")
		self.name = name
		self.house = house
	
	def __str__(self):
		return f"Hello, my name is {self.name} from {self.house}!"

def main():
	student = get_student()
	
	print(f"Hello, {student.name} from {student.house}!")

def get_student():
  return Student(input("Name: "), input("House: "))
  
    


if __name__ == "__main__":
	main()
      
	
