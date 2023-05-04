import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Calculate histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot histogram
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Histogram of Grayscale Image")
plt.show()

# Prompt user for threshold value
threshold = int(input("Enter threshold value: "))

# Apply thresholding to convert image to binary
binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Display binary image
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()