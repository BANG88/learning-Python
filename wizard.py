class Wizard:
	def __init__(self,name):
		if not name:
			raise ValueError("Wizard must have a name.")
		self.name = name



class Student(Wizard):
	def __init__(self, name, house):
		super().__init__(name)
		self.house = house



class Professor(Wizard):
	def	__init__(self, name, subject):
		super().__init__(name)
		self.subject = subject


wizard = Wizard("Merlin")
student = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus Snape", "Defense Against the Dark Arts")



print(student.name)