import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.

    Creates a negative effect by subtracting each pixel value from 255.
    White becomes black, black becomes white, etc.

    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Inverted image array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if array.ndim != 3:
        raise ValueError("Array must be 3-dimensional")
    if array.shape[2] != 3:
        raise ValueError("Array must have 3 color channels (RGB)")
    # Using allowed operators: =, +, -, *
    # Invert: 255 - pixel_value
    inverted = array.copy()
    inverted = 255 - inverted

    plt.figure(figsize=(10, 8))
    plt.imshow(inverted)
    plt.title("Inverted Image")
    plt.axis('off')
    plt.show()

    return inverted


def ft_red(array) -> np.ndarray:
    """
    Applies a red filter to the image.

    Keeps only the red channel, sets green and blue channels to 0.

    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Red-filtered image array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if array.ndim != 3:
        raise ValueError("Array must be 3-dimensional")
    if array.shape[2] != 3:
        raise ValueError("Array must have 3 color channels (RGB)")
    # Using allowed operators: =, *
    # Keep red channel, zero out others using multiplication
    red_filtered = array.copy()
    red_filtered = red_filtered * [1, 0, 0]

    plt.figure(figsize=(10, 8))
    plt.imshow(red_filtered)
    plt.title("Red Filter")
    plt.axis('off')
    plt.show()

    return red_filtered


def ft_green(array) -> np.ndarray:
    """
    Applies a green filter to the image.

    Keeps only the green channel, sets red and blue channels to 0.

    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Green-filtered image array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if array.ndim != 3:
        raise ValueError("Array must be 3-dimensional")
    if array.shape[2] != 3:
        raise ValueError("Array must have 3 color channels (RGB)")
    # Using allowed operators: =, -
    # Zero out red and blue by subtracting them from themselves
    green_filtered = array.copy()
    red = green_filtered[:, :, 0]
    blue = green_filtered[:, :, 2]
    green_filtered[:, :, 0] = red - red
    green_filtered[:, :, 2] = blue - blue

    plt.figure(figsize=(10, 8))
    plt.imshow(green_filtered)
    plt.title("Green Filter")
    plt.axis('off')
    plt.show()

    return green_filtered


def ft_blue(array) -> np.ndarray:
    """
    Applies a blue filter to the image.

    Keeps only the blue channel, sets red and green channels to 0.

    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Blue-filtered image array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if array.ndim != 3:
        raise ValueError("Array must be 3-dimensional")
    if array.shape[2] != 3:
        raise ValueError("Array must have 3 color channels (RGB)")
    # Using allowed operators: = (assignment only!)
    # Create new array and manually assign values
    blue_filtered = np.zeros_like(array)
    blue_filtered[:, :, 2] = array[:, :, 2]  # Copy only blue channel

    plt.figure(figsize=(10, 8))
    plt.imshow(blue_filtered)
    plt.title("Blue Filter")
    plt.axis('off')
    plt.show()

    return blue_filtered


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.

    Converts RGB image to grayscale by averaging the color channels.

    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Grayscale image array (3-channel with same values)
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if array.ndim != 3:
        raise ValueError("Array must be 3-dimensional")
    if array.shape[2] != 3:
        raise ValueError("Array must have 3 color channels (RGB)")
    # Using allowed operators: =, /
    # Average the RGB channels
    grey_filtered = array.copy()

    # Calculate average of RGB channels for each pixel
    red = grey_filtered[:, :, 0]
    green = grey_filtered[:, :, 1]
    blue = grey_filtered[:, :, 2]
    avg = (red + green + blue) / 3

    # Assign the average to all three channels
    grey_filtered[:, :, 0] = avg
    grey_filtered[:, :, 1] = avg
    grey_filtered[:, :, 2] = avg

    # Convert to uint8 to maintain proper image format
    grey_filtered = grey_filtered.astype(np.uint8)

    plt.figure(figsize=(10, 8))
    plt.imshow(grey_filtered)
    plt.title("Grey Filter")
    plt.axis('off')
    plt.show()

    return grey_filtered


def main():
    """
    Test function to demonstrate all filters.
    """
    try:
        array = ft_load("landscape.jpg")
        # Test all filters
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        # Print docstring as required
        print(ft_invert.__doc__)
    except FileNotFoundError as fnfe:
        print(f"File not found: {fnfe}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
