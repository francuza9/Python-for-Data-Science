def count_in_list(lst: list, value) -> int:
    """Count occurrences of value in the list."""
    try:
        if not isinstance(lst, list):
            raise TypeError("First argument must be a list")
        return lst.count(value)
    except TypeError as e:
        print(f"Error: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0
