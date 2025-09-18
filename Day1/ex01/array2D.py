import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list (list of lists) from start index to end index.

    Args:
        family (list): A 2D list where each inner list
            represents a family member's attributes.
        start (int): The starting index for slicing (inclusive).
        end (int): The ending index for slicing (exclusive).
    Returns:
        list: A sliced 2D list from start to end indices.
    Raises:
        ValueError: If the family list is empty or
             if inner lists are of varying lengths.
        TypeError: If the inputs are not of the expected types.
    """
    if not isinstance(family, list):
        raise TypeError("Family must be a list.")
    if not all(isinstance(member, list) for member in family):
        raise ValueError("All family members must be lists.")
    inner_list_size = len(family[0]) if family else 0
    if not all(len(member) == inner_list_size for member in family):
        raise ValueError("All family members must be of the same length.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers.")
    print(f"My shape is : {np.array(family).shape}")
    new_family = family[start:end]
    print(f"My new shape is : {np.array(new_family).shape}")
    return new_family
