def print_errors(kwargs: dict | None) -> None:
    """ Prints "ERROR" for each key in kwargs if kwargs is not None.

    Args:
        kwargs (dict | None): Dictionary of keyword arguments.
    """
    if kwargs is not None:
        for key in kwargs:
            print("ERROR")


def mean(
    data: list[float | int],
    data_length: int,
    print_flag: bool = True
) -> float:
    """ Calculates the mean of the data.

    Args:
        data (list[float | int]): List of numerical data.
        data_length (int): Length of the data list.
        print_flag (bool, optional): If True,
            prints the mean. Defaults to True.
    Returns:
        float: The mean of the data.
    Raises:
        TypeError: If data is not a list or contains
            non-numeric elements, or if print_flag is not a boolean.
        ValueError: If data_length is not a positive
            integer or if data contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise TypeError("Data should be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data should be int or float.")
    if data_length <= 0:
        raise ValueError("Data length should be a positive integer.")
    if not isinstance(print_flag, bool):
        raise TypeError("print_flag should be a boolean.")
    mean = sum(data) / data_length
    if print_flag:
        print(f"mean : {mean}")
    return mean


def median(data: list[float | int], data_length: int) -> float:
    """ Calculates the median of the data.

    Args:
        data (list[float | int]): List of numerical data.
        data_length (int): Length of the data list.
    Returns:
        float: The median of the data.
    Raises:
        TypeError: If data is not a list or contains non-numeric elements.
        ValueError: If data_length is not a positive integer
            or if data contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise TypeError("Data should be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data should be int or float.")
    if data_length <= 0:
        raise ValueError("Data length should be a positive integer.")
    mid = data_length // 2
    if data_length % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]
    print(f"median : {median}")
    return median


def quartile(data: list[float | int], data_length: int) -> tuple[float, float]:
    """ Calculates the first and third quartiles of the data.

    Args:
        data (list[float | int]): List of numerical data.
        data_length (int): Length of the data list.
    Returns:
        tuple[float, float]: The first and third quartiles of the data.
    Raises:
        TypeError: If data is not a list or contains non-numeric elements.
        ValueError: If data_length is not a positive integer
            or if data contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise TypeError("Data should be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data should be int or float.")
    if data_length <= 0:
        raise ValueError("Data length should be a positive integer.")
    q1_pos = (data_length - 1) * 0.25
    q3_pos = (data_length - 1) * 0.75

    q1_lower = int(q1_pos)
    q1_upper = q1_lower + 1 if q1_lower + 1 < data_length else q1_lower
    q1 = (q1_pos - q1_lower) * (data[q1_upper] - data[q1_lower])
    q1 = data[q1_lower] + q1

    q3_lower = int(q3_pos)
    q3_upper = q3_lower + 1 if q3_lower + 1 < data_length else q3_lower
    q3 = (q3_pos - q3_lower) * (data[q3_upper] - data[q3_lower])
    q3 = data[q3_lower] + q3
    print(f"quartile : [{q1}, {q3}]")
    return (q1, q3)


def standard_deviation(
    data: list[float | int],
    data_length: int,
    mean: float | int
) -> float:
    """ Calculates the standard deviation of the data.

    Args:
        data (list[float | int]): List of numerical data.
        data_length (int): Length of the data list.
        mean (float | int): Mean of the data.
    Returns:
        float: The standard deviation of the data.
    Raises:
        TypeError: If data is not a list or contains non-numeric elements,
            or if mean is not a number.
        ValueError: If data_length is not a positive integer
            or if data contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise TypeError("Data should be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data should be int or float.")
    if data_length <= 0:
        raise ValueError("Data length should be a positive integer.")
    if not isinstance(mean, (int, float)):
        raise TypeError("Mean should be a number.")
    variance = sum((x - mean) ** 2 for x in data) / data_length
    stddev = variance ** 0.5
    print(f"std : {stddev}")
    return stddev


def variance(
    data: list[float | int],
    data_length: int,
    mean: float | int
) -> float:
    """ Calculates the variance of the data.

    Args:
        data (list[float | int]): List of numerical data.
        data_length (int): Length of the data list.
        mean (float | int): Mean of the data.
    Returns:
        float: The variance of the data.
    Raises:
        TypeError: If data is not a list or contains non-numeric elements,
            or if mean is not a number.
        ValueError: If data_length is not a positive integer
            or if data contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise TypeError("Data should be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data should be int or float.")
    if data_length <= 0:
        raise ValueError("Data length should be a positive integer.")
    if not isinstance(mean, (int, float)):
        raise TypeError("Mean should be a number.")
    variance = sum((x - mean) ** 2 for x in data) / data_length
    print(f"var : {variance}")
    return variance


def ft_statistics(*args, **kwargs) -> None:
    """ Computes and prints statistical measures
    based on provided data and operations.

    Args:
        *args: Variable length argument list of numerical data.
        **kwargs: Keyword arguments specifying statistical
            operations to perform.
    """
    try:
        if not args:
            print_errors(kwargs)
            return

        validate_data = []
        for arg in args:
            if isinstance(arg, (int, float)):
                validate_data.append(arg)
            else:
                print_errors(kwargs)
                return

        data = validate_data
        data_sorted = sorted(data)
        data_length = len(data)

        name_to_func = {
            'mean': mean,
            'median': median,
            'quartile': quartile,
            'std': standard_deviation,
            'var': variance
        }

        for key, operation in kwargs.items():
            if operation in name_to_func:
                if operation in ('std', 'var'):
                    try:
                        name_to_func[operation](
                            data_sorted,
                            data_length,
                            mean(data_sorted, data_length, False)
                        )
                    except TypeError as e:
                        print(f"Type ERROR: {e}")
                    except ValueError as e:
                        print(f"Value ERROR: {e}")
                    except Exception as e:
                        print(f"ERROR: {e}")
                else:
                    try:
                        name_to_func[operation](data_sorted, data_length)
                    except TypeError as e:
                        print(f"Type ERROR: {e}")
                    except ValueError as e:
                        print(f"Value ERROR: {e}")
                    except Exception as e:
                        print(f"ERROR: {e}")
            else:
                pass
    except TypeError as e:
        print(f"Type ERROR: {e}")
    except ValueError as e:
        print(f"Value ERROR: {e}")
    except Exception as e:
        print(f"ERROR: {e}")
