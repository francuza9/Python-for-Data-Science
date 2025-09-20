import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D array without using library transpose functions.

    Args:
        array (np.ndarray): 2D array to transpose
    Returns:
        np.ndarray: Transposed array with swapped dimensions
    Raises:
        TypeError: If input is not a numpy array
        ValueError: If input is not 2D
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    if array.ndim != 2:
        raise ValueError("Input must be a 2D array.")
    rows, cols = array.shape
    transposed = np.zeros((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = array[i, j]
    return transposed


def crop_square(img: np.ndarray) -> np.ndarray:
    """
    Crop a square region from the center of the image and convert to grayscale.

    Args:
        img (np.ndarray): Input RGB image
    Returns:
        np.ndarray: Cropped square grayscale image
    Raises:
        ValueError: If image dimensions are invalid
    """
    if img.ndim != 3:
        raise ValueError("Image must be 3D (height, width, channels)")
    height, width = img.shape[:2]
    square_size = min(height, width)
    start_row = (height - square_size) // 2
    start_col = (width - square_size) // 2
    cropped = img[
        start_row:start_row + square_size,
        start_col:start_col + square_size
    ]
    # Convert to grayscale using proper RGB weights
    grayscale = np.dot(cropped[..., :3], [0.2989, 0.5870, 0.1140])
    grayscale = grayscale.astype(np.uint8)
    return grayscale


def display_img(img: np.ndarray, title: str = "Image") -> None:
    """
    Display the image using matplotlib.

    Args:
        img (np.ndarray): Image to display
        title (str): Title for the plot
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.show()


def main() -> None:
    """
    Main function to load image, crop square, transpose and display.
    """
    try:
        img = ft_load("animal.jpeg")
        print(img)
        square_img = crop_square(img)
        print(f"The shape of image is: {square_img.shape}")
        print(square_img)
        transposed_img = manual_transpose(square_img)
        print(f"New shape after Transpose: {transposed_img.shape}")
        print(transposed_img)
        display_img(transposed_img, "Transposed Image")
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
