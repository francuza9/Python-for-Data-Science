import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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
