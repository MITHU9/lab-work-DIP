from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img = Image.open('leuvenA.jpg')

# Get image dimensions
width, height = img.size

# Divide the image into 4 quadrants
left_upper = img.crop((0, 0, width // 2, height // 2))  # Top-left
right_upper = img.crop((width // 2, 0, width, height // 2))  # Top-right
left_lower = img.crop((0, height // 2, width // 2, height))  # Bottom-left
right_lower = img.crop((width // 2, height // 2, width, height))  # Bottom-right

# Plot the original image and the 4 segments
fig, axes = plt.subplots(1, 5, figsize=(20, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(left_upper)
axes[1].set_title("Top Left")
axes[1].axis('off')

axes[2].imshow(right_upper)
axes[2].set_title("Top Right")
axes[2].axis('off')

axes[3].imshow(left_lower)
axes[3].set_title("Bottom Left")
axes[3].axis('off')

axes[4].imshow(right_lower)
axes[4].set_title("Bottom Right")
axes[4].axis('off')

plt.show()

# Merge them back in the original order
merged_img = Image.new('RGB', (width, height))
merged_img.paste(left_upper, (0, 0))  # Top-left
merged_img.paste(right_upper, (width // 2, 0))  # Top-right
merged_img.paste(left_lower, (0, height // 2))  # Bottom-left
merged_img.paste(right_lower, (width // 2, height // 2))  # Bottom-right

# Plot the merged image
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(merged_img)
axes[1].set_title("Merged Image")
axes[1].axis('off')

plt.show()
