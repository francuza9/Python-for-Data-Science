from S1E9 import Character

class Baratheon(Character):
	def __init__(self, first_name: str, is_alive: bool = True):
		try:
			super().__init__(first_name, is_alive)
		except TypeError as e:
			print(f"Error initializing Baratheon: {e}")
			raise
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"

	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
	
	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def die(self):
		self.is_alive = False


class Lannister(Character):
	def __init__(self, first_name: str, is_alive: bool = True):
		try:
			super().__init__(first_name, is_alive)
		except TypeError as e:
			print(f"Error initializing Lannister: {e}")
			raise
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"
	
	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
	
	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
	
	def die(self):
		self.is_alive = False

	@classmethod
	def create_lannister(cls, first_name: str, is_alive: bool = True):
		return cls(first_name, is_alive)
