import cv2
import matplotlib.pyplot as plt

image_path = 'leuvenA.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not loaded. Please check the file path.")
    exit()


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
colors = ('b', 'g', 'r')


for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)

plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.show()