import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Calculate histogram using OpenCV's histogram function
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot histogram using matplotlib
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Histogram of Grayscale Image (using matplotlib)")
plt.show()

# Plot histogram using OpenCV's plot function
plt.plot(hist)
plt.title("Histogram of Grayscale Image (using OpenCV)")
plt.show()