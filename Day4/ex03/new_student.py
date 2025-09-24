import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
	return ''.join(random.choices(string.ascii_letters + string.digits, k=15))

@dataclass
class Student:
	name: str
	surname: str
	active: bool = True
	login: str = field(init=False)
	id: str = field(default_factory=generate_id, init=False)

	def __post_init__(self):
		""" Post-initialization to set up login and validate fields.

		Raises:
			ValueError: If name or surname is empty.
			TypeError: If name or surname is not a string.
		"""
		if not self.name or not self.surname:
			raise ValueError("Name and surname cannot be empty.")
		if not isinstance(self.name, str) or not isinstance(self.surname, str):
			raise TypeError("Name and surname must be strings.")
		if len(self.name) < 1:
			raise ValueError("Name must be at least 1 character long.")
		self.login = (self.name[0] + self.surname)