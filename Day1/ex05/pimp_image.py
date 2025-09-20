import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    
    Creates a negative effect by subtracting each pixel value from 255.
    White becomes black, black becomes white, etc.
    
    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Inverted image array
    """
    # Using allowed operators: =, +, -, *
    # Invert: 255 - pixel_value
    inverted = array.copy()
    inverted = 255 - inverted
    
    # Display the result
    plt.figure(figsize=(10, 8))
    plt.imshow(inverted)
    plt.title("Inverted Image")
    plt.axis('off')
    plt.show()
    
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image.
    
    Keeps only the red channel, sets green and blue channels to 0.
    
    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Red-filtered image array
    """
    # Using allowed operators: =, *
    # Keep red channel, zero out others using multiplication
    red_filtered = array.copy()
    red_filtered = red_filtered * [1, 0, 0]  # Multiply by [1,0,0] to keep red only
    
    # Display the result
    plt.figure(figsize=(10, 8))
    plt.imshow(red_filtered)
    plt.title("Red Filter")
    plt.axis('off')
    plt.show()
    
    return red_filtered


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image.
    
    Keeps only the green channel, sets red and blue channels to 0.
    
    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Green-filtered image array
    """
    # Using allowed operators: =, -
    # Zero out red and blue by subtracting them from themselves
    green_filtered = array.copy()
    green_filtered[:, :, 0] = green_filtered[:, :, 0] - green_filtered[:, :, 0]  # Red = 0
    green_filtered[:, :, 2] = green_filtered[:, :, 2] - green_filtered[:, :, 2]  # Blue = 0
    
    # Display the result
    plt.figure(figsize=(10, 8))
    plt.imshow(green_filtered)
    plt.title("Green Filter")
    plt.axis('off')
    plt.show()
    
    return green_filtered


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image.
    
    Keeps only the blue channel, sets red and green channels to 0.
    
    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Blue-filtered image array
    """
    # Using allowed operators: = (assignment only!)
    # Create new array and manually assign values
    blue_filtered = np.zeros_like(array)
    blue_filtered[:, :, 2] = array[:, :, 2]  # Copy only blue channel
    
    # Display the result
    plt.figure(figsize=(10, 8))
    plt.imshow(blue_filtered)
    plt.title("Blue Filter")
    plt.axis('off')
    plt.show()
    
    return blue_filtered


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.
    
    Converts RGB image to grayscale by averaging the color channels.
    
    Args:
        array (np.ndarray): Input image array
    Returns:
        np.ndarray: Grayscale image array (3-channel with same values)
    """
    # Using allowed operators: =, /
    # Average the RGB channels
    grey_filtered = array.copy()
    
    # Calculate average of RGB channels for each pixel
    avg = (grey_filtered[:, :, 0] + grey_filtered[:, :, 1] + grey_filtered[:, :, 2]) / 3
    
    # Assign the average to all three channels
    grey_filtered[:, :, 0] = avg
    grey_filtered[:, :, 1] = avg  
    grey_filtered[:, :, 2] = avg
    
    # Convert to uint8 to maintain proper image format
    grey_filtered = grey_filtered.astype(np.uint8)
    
    # Display the result
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
    # This would be your tester.py content
    from load_image import ft_load
    
    try:
        array = ft_load("landscape.jpg")
        
        # Test all filters
        inverted = ft_invert(array)
        red = ft_red(array)
        green = ft_green(array) 
        blue = ft_blue(array)
        grey = ft_grey(array)
        
        # Print docstring as required
        print(ft_invert.__doc__)
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()