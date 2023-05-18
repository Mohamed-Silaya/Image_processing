import cv2
import numpy as np

# Load image
img = cv2.imread('rr.jpg')

# Apply 3x3 median filter
median3 = cv2.medianBlur(img, 3)

# Apply 5x5 median filter
median5 = cv2.medianBlur(img, 5)

# Apply 3x3 mean filter
kernel3 = np.ones((3,3),np.float32)/9
mean3 = cv2.filter2D(img,-1,kernel3)

# Apply 7x7 mean filter
kernel7 = np.ones((7,7),np.float32)/49
mean7 = cv2.filter2D(img,-1,kernel7)

# Display original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('3x3 Median Filter', median3)
cv2.imshow('5x5 Median Filter', median5)
cv2.imshow('3x3 Mean Filter', mean3)
cv2.imshow('7x7 Mean Filter', mean7)
cv2.waitKey(0)
cv2.destroyAllWindows()