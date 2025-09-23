class calculator:

	def __init__(self, values: list[float | int]):
		self.values = values

	def __add__(self, object) -> None:
		if not isinstance(object, (int, float)):
			raise TypeError("Operand must be an integer or a float")
		self.values = [value + object for value in self.values]
		print(self.values)
	
	def __mul__(self, object) -> None:
		if not isinstance(object, (int, float)):
			raise TypeError("Operand must be an integer or a float")
		self.values = [value * object for value in self.values]
		print(self.values)

	def __sub__(self, object) -> None:
		if not isinstance(object, (int, float)):
			raise TypeError("Operand must be an integer or a float")
		self.values = [value - object for value in self.values]
		print(self.values)

	def __truediv__(self, object) -> None:
		if not isinstance(object, (int, float)):
			raise TypeError("Operand must be an integer or a float")
		if object == 0:
			raise ZeroDivisionError("Division by zero is not allowed")
		self.values = [value / object for value in self.values]
		print(self.values)
