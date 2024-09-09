import cv2
import numpy as np

# Ensure that the correct image path is provided
image_path = 'leuvenA.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or path is incorrect")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # The image is already a NumPy array, no need to convert it again
    image_array = gray_image

    print("2D Array of the image (Grayscale values):\n", image_array)

    rows, cols = image_array.shape

    # Accessing the corner elements
    top_left = image_array[0, 0]
    top_right = image_array[0, cols - 1]
    bottom_left = image_array[rows - 1, 0]
    bottom_right = image_array[rows - 1, cols - 1]

    # Printing corner elements
    print("\nCorner elements:")
    print("Top-left:", top_left)
    print("Top-right:", top_right)
    print("Bottom-left:", bottom_left)
    print("Bottom-right:", bottom_right)

    # Calculating the sum of corner elements
    corner_sum = top_left + top_right + bottom_left + bottom_right
    print("\nSum of the corner elements:", corner_sum)