from abc import ABC, abstractmethod

class Character(ABC):
	""" Character Docstring """
	def __init__(self, first_name: str, is_alive: bool = True):
		""" Character init method """
		if not isinstance(first_name, str):
			raise TypeError("first_name must be a string")
		if not isinstance(is_alive, bool):
			raise TypeError("is_alive must be a boolean")
		self.first_name = first_name
		self.is_alive = is_alive
	
	@abstractmethod
	def die(self):
		""" Abstract method to be implemented by subclasses """
		pass


class Stark(Character):
	""" Stark Docstring """
	def __init__(self, first_name: str, is_alive: bool = True):
		""" Stark init method """
		try:
			super().__init__(first_name, is_alive)
		except TypeError as e:
			print(f"Error initializing Stark: {e}")
			raise

	def die(self):
		""" Method to set is_alive to False """
		self.is_alive = False
		# print(f"{self.first_name} Stark has died.")