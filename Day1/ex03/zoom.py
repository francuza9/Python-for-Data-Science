import numpy as np
# import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_img(
    img: np.ndarray,
    x1: int, x2: int,
    y1: int, y2: int,
    z1: int, z2: int
) -> np.ndarray:
    """
    Zoom into a specific region of the image.

    Args:
        img (np.ndarray): The original image as a NumPy array.
        x1 (int): The starting x-coordinate (inclusive).
        x2 (int): The ending x-coordinate (exclusive).
        y1 (int): The starting y-coordinate (inclusive).
        y2 (int): The ending y-coordinate (exclusive).
        z1 (int): The starting z-coordinate (inclusive).
        z2 (int): The ending z-coordinate (exclusive).
    Returns:
        np.ndarray: The zoomed-in region of the image.
    Raises:
        TypeError: If the input image is not a
            numpy array or if coordinates are not integers.
        ValueError: If the input image is not 3-dimensional.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Image must be a numpy array.")
    if img.ndim != 3:
        raise ValueError("Image must be a 3D array.")
    if not all(isinstance(i, int) for i in [x1, x2, y1, y2, z1, z2]):
        raise TypeError("Coordinates must be integers.")
    return img[y1:y2, x1:x2, z1:z2]


def display_img(img: np.ndarray) -> None:
    """
    Display the image using matplotlib.

    Args:
        img (np.ndarray): The image to be displayed.
    Returns:
        None
    Raises:
        TypeError: If the input is not a numpy array.
        ValueError: If the input array is not 3-dimensional.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Image must be a numpy array.")
    if img.ndim != 3:
        raise ValueError("Image must be a 3D array.")
    plt.imshow(img)
    # plt.xlabel("Width hello")
    # plt.ylabel("Height hello")
    plt.show()


def main():
    """
    Main function to load, zoom, and display an image.
    """
    try:
        img = ft_load("animal.jpeg")
        print(img)
        img = zoom_img(img, 100, 500, 100, 500, 0, 1)
        squeezed_img = np.squeeze(img) if \
            img.ndim == 3 and img.shape[2] == 1 else img
        print(f"New shape after slicing: {img.shape} or {squeezed_img.shape}")
        print(img)
        display_img(img)
    except TypeError as te:
        print("TypeError:", te)
    except ValueError as ve:
        print("ValueError:", ve)
    except FileNotFoundError as fnfe:
        print("FileNotFoundError:", fnfe)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
