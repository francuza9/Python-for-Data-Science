import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified file path and convert it to RGB format.

    Args:
        path (str): The file path to the image.
    Returns:
        np.ndarray: The image in RGB format as a NumPy array.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("The path must be a string.")
        img = cv2.imread(path)
        if img is None:
            raise FileNotFoundError(f"Image not found at path: {path}")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img_rgb.size == 0:
            raise ValueError("The image is empty.")
        print("The shape of image is:", img_rgb.shape)
        return img_rgb
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return np.array([])
    except TypeError as e:
        print(f"Error: {e}")
        return np.array([])
    except ValueError as e:
        print(f"Error: {e}")
        return np.array([])
    except Exception as e:
        print(f"Unexpected error: {e}")
        return np.array([])
