def callLimit(limit: int):
    """ Returns a decorator that limits the number of times
    a function can be called.

    Args:
        limit (int): The maximum number of times the function can be called.
    Returns:
        function: A decorator that limits the number of times
            a function can be called.
    Raises:
        TypeError: If limit is not an integer or if the decorated
            object is not a function.
        ValueError: If limit is not a positive integer.
    """
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit should be an integer.")
        if limit <= 0:
            raise ValueError("Limit should be a positive integer.")
        count = 0

        def callLimiter(function):
            if not callable(function):
                raise TypeError("Input should be a function.")

            def limit_function(*args, **kwds):
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    print(f"Error: {function} call too many times")
            return limit_function
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return callLimiter
