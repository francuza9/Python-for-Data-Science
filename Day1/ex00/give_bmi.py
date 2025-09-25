import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a
    list of heights (in cm) and weights (in kg).

    Args:
        height (list[int | float]): A list of heights in centimeters.
        weight (list[int | float]): A list of weights in kilograms.
    Returns:
        list[int | float]: A list of BMI values corresponding
            to the input heights and weights.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must"
                             " be of the same length.")
        if not height or not weight:
            raise ValueError("Height and weight lists must not be empty.")
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Height and weight must be provided as lists.")
        if not all(isinstance(h, (int, float)) and h > 0 for h in height):
            raise ValueError("All height values must be positive numbers.")
        if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
            raise ValueError("All weight values must be positive numbers.")
        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / (height_array ** 2)
        return bmi.tolist()
    except ValueError as e:
        print(f"Error: {e}")
        return []
    except TypeError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values, returning a
    list of booleans indicating if each BMI exceeds the limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The BMI limit to compare against.
    Returns:
        list[bool]: A list of booleans where
            True indicates the BMI exceeds the limit.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI must be provided as a list.")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise ValueError("All BMI values must be numbers.")
        if not isinstance(limit, (int)) or limit <= 0:
            raise TypeError("Limit must be a positive number.")
        bmi_array = np.array(bmi)
        return (bmi_array > limit).tolist()
    except TypeError as e:
        print(f"Error: {e}")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
