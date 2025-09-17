
def ft_filter(function_to_apply, iterable):
    """filter(function or None, iterable) --> filter object"""
    if function_to_apply is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function_to_apply(item)]
