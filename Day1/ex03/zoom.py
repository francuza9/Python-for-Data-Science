import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_img(
    img: np.ndarray,
    y1: int, y2: int,
    x1: int, x2: int
) -> np.ndarray:
    """
    Zoom into a specific region of the image and convert to grayscale.

    Args:
        img (np.ndarray): The original image as a NumPy array.
        y1 (int): The starting row (inclusive).
        y2 (int): The ending row (exclusive).
        x1 (int): The starting column (inclusive).
        x2 (int): The ending column (exclusive).
    Returns:
        np.ndarray: The zoomed-in grayscale region of the image.
    Raises:
        TypeError: If the input image is not a
            numpy array or coordinates are not integers.
        ValueError: If the input image is not 3-dimensional.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Image must be a numpy array.")
    if img.ndim != 3:
        raise ValueError("Image must be a 3D array.")
    if not all(isinstance(i, int) for i in [y1, y2, x1, x2]):
        raise TypeError("Coordinates must be integers.")
    cropped = img[y1:y2, x1:x2]
    # Convert to grayscale using RGB weights
    grayscale = np.dot(cropped[..., :3], [0.2989, 0.5870, 0.1140])
    grayscale = grayscale.astype(np.uint8)
    # Add back the channel dimension to make it (height, width, 1)
    grayscale = grayscale[:, :, np.newaxis]
    return grayscale


def display_img(img: np.ndarray) -> None:
    """
    Display the image using matplotlib with axis labels.

    Args:
        img (np.ndarray): The image to be displayed.
    Returns:
        None
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Image must be a numpy array.")
    if img.ndim == 3 and img.shape[2] == 1:
        display_array = img.squeeze()
        plt.imshow(display_array, cmap='gray')
    elif img.ndim == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.show()


def main():
    """
    Main function to load, zoom, and display an image.
    """
    try:
        img = ft_load("animal.jpeg")
        print(img)
        zoomed_img = zoom_img(img, 100, 500, 100, 500)
        # Create squeezed version for shape comparison
        squeezed_img = np.squeeze(zoomed_img)
        print(f"New shape after slicing: {zoomed_img.shape}", end="")
        print(f" or {squeezed_img.shape}")
        print(zoomed_img)
        display_img(zoomed_img)
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
