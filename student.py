class Student:
	def __init__(self, name, house):
		if not name:
			raise ValueError("Name is required")
		if not house:
			raise ValueError("House is required")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is invalid")
		self.name = name
		self._house = house
	
	def __str__(self):
		return f"Hello, my name is {self.name} from {self.house}!"
	
	@property
	def house(self):
		return self._house
	
	@house.setter
	def house(self, house):
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("House is invalid")
		self.house = house

def main():
	student = get_student()
	
	print(student)

def get_student():
  return Student(input("Name: "), input("House: "))
  
    


if __name__ == "__main__":
	main()
      
	
