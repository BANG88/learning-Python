class Vault:
	def __init__(self,gallons = 0,sickles = 0,knuts = 0):
		self.gallons = gallons
		self.sickles = sickles
		self.knuts = knuts
	
	def __str__(self):
		return f"{self.gallons} gallons, {self.sickles} sickles, {self.knuts} knuts"
	
	def __add__(self,other):
		gallons = self.gallons + other.gallons
		sickles = self.sickles + other.sickles
		knuts = self.knuts + other.knuts
		return Vault(gallons,sickles,knuts)
	



potter = Vault(100,100,100)
print(potter)

weasley = Vault(10,10,10)
print(weasley)

print(potter + weasley)


print(potter + str())


	



