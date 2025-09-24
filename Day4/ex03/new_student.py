import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """ Generates a random alphanumeric ID of length 15. """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=15))


@dataclass
class Student:
    """ Represents a student with personal and academic details.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name of the student.
        active (bool): Indicates if the student is
            currently active. Default is True.
        login (str): The login identifier for the
            student, generated from name and surname.
        id (str): A unique identifier for the student,
            generated automatically.
    """
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
