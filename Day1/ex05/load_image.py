import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified file path and convert it to RGB format.

    Args:
        path (str): The file path to the image.
    Returns:
        np.ndarray: The image in RGB format as a NumPy array.
    Raises:
        FileNotFoundError: If the image file
            does not exist at the specified path.
        ValueError: If the image is empty or cannot be loaded.
        TypeError: If the path is not a string.
    """
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
