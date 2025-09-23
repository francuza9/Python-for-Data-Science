def square(x: int | float) -> int | float:
    """ Returns the square of a number.

    Args:
        x (int | float): The number to be squared.
    Returns:
        int | float: The square of the number.
    Raises:
        TypeError: If x is not a number.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input should be a number.")
    return x * x


def pow(x: int | float) -> int | float:
    """ Returns the number raised to the power of itself.

    Args:
        x (int | float): The number to be raised to the power of itself.
    Returns:
        int | float: The number raised to the power of itself.
    Raises:
        TypeError: If x is not a number.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input should be a number.")
    return x ** x


def outer(x: int | float, function) -> object:
    """ Returns a counter function that applies the given function to x

    Args:
        x (int | float): The initial value.
        function (function): The function to be applied to x.
    Returns:
        object: A counter function that applies the given function to x.
    Raises:
        TypeError: If x is not a number or if function is not a function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input should be a number.")
    if not callable(function):
        raise TypeError("Input should be a function.")
    count = 0

    def inner() -> float:
        """ Applies the given function to x and increments the counter.
        [CLOSURE]
        Returns:
            float: The result of applying the function to x.
        """
        nonlocal count, x
        x = function(x)
        count += 1
        return x
    return inner
