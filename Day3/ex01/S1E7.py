from S1E9 import Character


class Baratheon(Character):
    """ Baratheon Class inheriting from Character

    Attributes:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize Baratheon with first_name and is_alive status

        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        Raises:
            TypeError: If first_name is not a string
                or is_alive is not a boolean.
        """
        try:
            super().__init__(first_name, is_alive)
        except TypeError as e:
            print(f"Error initializing Baratheon: {e}")
            raise
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """ String representation of the Baratheon character """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """ Official string representation of the Baratheon character """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """ Set the Baratheon character's is_alive status to False """
        self.is_alive = False


class Lannister(Character):
    """ Lannister Class inheriting from Character

    Attributes:
        first_name (str): The first name of the Lannister character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize Lannister with first_name and is_alive status

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        Raises:
            TypeError: If first_name is not a string
                or is_alive is not a boolean.
        """
        try:
            super().__init__(first_name, is_alive)
        except TypeError as e:
            print(f"Error initializing Lannister: {e}")
            raise
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """ String representation of the Lannister character """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """ Official string representation of the Lannister character """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """ Set the Lannister character's is_alive status to False """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """ Create a new Lannister character
            [@classmethod]
        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        Returns:
            Lannister: A new instance of Lannister.
        """
        return cls(first_name, is_alive)
