class calculator:
    """ A simple calculator class that performs arithmetic operations
    on a list of numerical values.

    Attributes:
        values (list of float | int): The list
            of numerical values to operate on.
    """

    def __init__(self, values: list[float | int]):
        """ Initialize the calculator with a list of numerical values.

        Args:
            values (list of float | int): The list
                of numerical values to operate on.
        Raises:
            TypeError: If values is not a list or contains non-numeric types.
        """
        if not isinstance(values, list):
            raise TypeError("values must be a list")
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("All elements in values must"
                                " be integers or floats")
        self.values = values

    def __add__(self, object) -> None:
        """ Add a number to each element in the
            values list and print the result.

        Args:
            object (int | float): The number to add to each element.
        Raises:
            TypeError: If object is not an integer or a float.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Operand must be an integer or a float")
        self.values = [value + object for value in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """ Multiply each element in the values
            list by a number and print the result.

        Args:
            object (int | float): The number to multiply each element by.
        Raises:
            TypeError: If object is not an integer or a float.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Operand must be an integer or a float")
        self.values = [value * object for value in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """ Subtract a number from each element in
            the values list and print the result.

        Args:
            object (int | float): The number to subtract from each element.
        Raises:
            TypeError: If object is not an integer or a float.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Operand must be an integer or a float")
        self.values = [value - object for value in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """ Divide each element in the values list
        by a number and print the result.

        Args:
            object (int | float): The number to divide each element by.
        Raises:
            TypeError: If object is not an integer or a float.
            ZeroDivisionError: If object is zero.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Operand must be an integer or a float")
        if object == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        self.values = [value / object for value in self.values]
        print(self.values)
