import math

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)
	def __abs__(self):
		return math.hypot(self.x, self.y)
	def __bool__(self):
		return bool(self.x or self.y)
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)
	

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1+v2)