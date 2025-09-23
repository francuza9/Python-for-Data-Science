def callLimit(limit: int):
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
    return callLimiter
