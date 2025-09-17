
def ft_filter(function_to_apply, iterable):
    """Filters elements from an iterable based on a predicate function."""
    if function_to_apply is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function_to_apply(item)]
