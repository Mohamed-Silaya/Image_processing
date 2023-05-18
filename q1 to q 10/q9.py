import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Get image resolution and bit depth
height, width, channels = input_image.shape
bit_depth = input_image.dtype.itemsize * 8

print("Image resolution:", width, "x", height)
print("Bit depth:", bit_depth)

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Calculate histogram
hist, bins = np.histogram(gray_image.ravel(), 256, [0, 256])

# Plot histogram
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Histogram of Grayscale Image")
plt.show()

# Calculate normalized histogram
hist_norm = hist / (height * width)

# Plot normalized histogram
plt.plot(hist_norm)
plt.title("Normalized Histogram of Grayscale Image")
plt.show()

# Calculate cumulative histogram
hist_cumsum = np.cumsum(hist_norm)

# Plot cumulative histogram
plt.plot(hist_cumsum)
plt.title("Cumulative Histogram of Grayscale Image")
plt.show()

# Perform histogram equalization
hist_equalized = cv2.equalizeHist(gray_image)

# Display equalized image and histogram
cv2.imshow("Equalized Image", hist_equalized)
plt.hist(hist_equalized.ravel(), 256, [0, 256])
plt.title("Histogram of Equalized Image")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()