from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self._eyes = self.eyes
        self._hairs = self.hairs

    def set_eyes(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.hairs = color

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs

    @property
    def eyes(self) -> str:
        return self._eyes
    
    @property
    def hairs(self) -> str:
        return self._hairs

    @eyes.setter
    def eyes(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self._eyes = color
    
    @hairs.setter
    def hairs(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self._hairs = color
