from abc import ABC, abstractmethod


class Character(ABC):
    """ Abstract Character Class

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize Character with first_name and is_alive status

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        """
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ Abstract method to set the character's is_alive status to False """
        pass


class Stark(Character):
    """ Stark Class inheriting from Character

    Attributes:
        first_name (str): The first name of the Stark character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize Stark with first_name and is_alive status

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """ Set the Stark character's is_alive status to False """
        self.is_alive = False
