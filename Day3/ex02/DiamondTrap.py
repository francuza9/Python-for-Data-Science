from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ King Class inheriting from Baratheon and Lannister

    Attributes:
        first_name (str): The first name of the King character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.
        eyes (str): The eye color of the King character.
        hairs (str): The hair color of the King character.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Initialize King with first_name, is_alive status, eyes and hairs

        Args:
            first_name (str): The first name of the King character.
            is_alive (bool, optional): Indicates if
                the character is alive. Defaults to True.
        Raises:
            TypeError: If first_name is not a string
                or is_alive is not a boolean.
        """
        super().__init__(first_name, is_alive)
        self._eyes = self.eyes
        self._hairs = self.hairs

    def set_eyes(self, color: str) -> None:
        """ Set the eye color of the King character

        Args:
            color (str): The eye color to set.
        Raises:
            TypeError: If color is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """ Set the hair color of the King character

        Args:
            color (str): The hair color to set.
        Raises:
            TypeError: If color is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.hairs = color

    def get_eyes(self) -> str:
        """ Get the eye color of the King character

        Returns:
            str: The eye color of the King character.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """ Get the hair color of the King character

        Returns:
            str: The hair color of the King character.
        """
        return self.hairs

    @property
    def eyes(self) -> str:
        """ Get the eye color of the King character

        Returns:
            str: The eye color of the King character.
        """
        return self._eyes

    @property
    def hairs(self) -> str:
        """ Get the hair color of the King character

        Returns:
            str: The hair color of the King character.
        """
        return self._hairs

    @eyes.setter
    def eyes(self, color: str) -> None:
        """ Set the eye color of the King character

        Args:
            color (str): The eye color to set.
        Raises:
            TypeError: If color is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self._eyes = color

    @hairs.setter
    def hairs(self, color: str) -> None:
        """ Set the hair color of the King character

        Args:
            color (str): The hair color to set.
        Raises:
            TypeError: If color is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self._hairs = color
