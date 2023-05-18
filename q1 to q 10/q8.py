import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Apply 3x3 median filter
median_3x3 = cv2.medianBlur(gray_image, 3)

# Apply 5x5 median filter
median_5x5 = cv2.medianBlur(gray_image, 5)

# Define 3x3 kernel for mean filter
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# Define 7x7 kernel for mean filter
kernel_7x7 = np.ones((7, 7), np.float32) / 49

# Apply 3x3 mean filter
mean_3x3 = cv2.filter2D(gray_image, -1, kernel_3x3)

# Apply 7x7 mean filter
mean_7x7 = cv2.filter2D(gray_image, -1, kernel_7x7)

# Display results
plt.subplot(2, 3, 1), plt.imshow(gray_image, cmap="gray"), plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(median_3x3, cmap="gray"), plt.title("Median (3x3)")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3), plt.imshow(median_5x5, cmap="gray"), plt.title("Median (5x5)")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 5), plt.imshow(mean_3x3, cmap="gray"), plt.title("Mean (3x3)")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 6), plt.imshow(mean_7x7, cmap="gray"), plt.title("Mean (7x7)")
plt.xticks([]), plt.yticks([])
plt.show()