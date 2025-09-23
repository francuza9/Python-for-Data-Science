class calculator:
    """ A simple calculator class to perform
        basic operations on vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Calculate the dot product of two vectors and print the result.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        Raises:
            ValueError: If the vectors are not of the same length.
        """
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ Calculate the sum of two vectors and print the result.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        Raises:
            ValueError: If the vectors are not of the same length.
        """
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ Calculate the difference of two vectors and print the result.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        Raises:
            ValueError: If the vectors are not of the same length.
        """
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
