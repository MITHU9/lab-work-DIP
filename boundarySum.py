import cv2
import numpy as np

# Step 1: Read the image using OpenCV
image_path = 'leuvenA.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Convert the grayscale image to a 2D array
image_array = np.array(gray_image)

# Get the dimensions of the array
rows, cols = image_array.shape

# Step 4: Extract the boundary elements
top_boundary = image_array[0, :]  # Top row
bottom_boundary = image_array[rows - 1, :]  # Bottom row
left_boundary = image_array[1:rows - 1, 0]  # Left column (excluding corners)
right_boundary = image_array[1:rows - 1, cols - 1]  # Right column (excluding corners)

# Combine all boundary elements into a single array
boundary_elements = np.concatenate((top_boundary, bottom_boundary, left_boundary, right_boundary))

# Print the boundary elements
print("Boundary elements of the image:\n", boundary_elements)

# Step 5: Calculate the sum of the boundary elements
boundary_sum = np.sum(boundary_elements)

# Print the sum of the boundary elements
print("\nSum of the boundary elements:",boundary_sum)