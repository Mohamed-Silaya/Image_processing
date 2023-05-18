import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Apply automatic thresholding using OpenCV's built-in function
_, binary_image_cv = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Calculate histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot histogram
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Histogram of Grayscale Image")
plt.show()

# Apply automatic thresholding using Otsu's method
def otsu_threshold(image):
    # Compute histogram
    hist, bins = np.histogram(image, bins=256, range=(0, 256))

    # Compute normalized histogram and cumulative sum
    p = hist.astype(np.float32) / np.sum(hist)
    s = np.cumsum(p)

    # Compute mean and variance for all possible thresholds
    mean = np.cumsum(p * np.arange(0, 256))
    mean_t = mean[-1]
    var = np.cumsum(p * (np.arange(0, 256) - mean_t)**2)

    # Compute between-class variance and find optimal threshold
    bcv = (mean_t * s - mean)**2 / (s * (1 - s))
    threshold = np.argmax(bcv)

    # Apply thresholding to convert image to binary
    binary_image = np.zeros_like(image)
    binary_image[image > threshold] = 255

    return binary_image

binary_image_otsu = otsu_threshold(gray_image)

# Display binary images
cv2.imshow("Binary Image (OpenCV)", binary_image_cv)
cv2.imshow("Binary Image (Otsu)", binary_image_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()