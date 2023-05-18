import cv2
import numpy as np
import math
import os

# Read input image
input_image = cv2.imread("Old-Pic.png")

# Convert to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Ask user for batch size
batch_size = int(input("Enter batch size: "))

# Calculate number of rows and columns for batches
num_rows = math.ceil(gray_image.shape[0] / batch_size)
num_cols = math.ceil(gray_image.shape[1] / batch_size)

# Create directory to store batches
if not os.path.exists("batches"):
    os.makedirs("batches")

# Divide image into batches
batches = []
for i in range(num_rows):
    row_batches = []
    for j in range(num_cols):
        batch = gray_image[i*batch_size:(i+1)*batch_size, j*batch_size:(j+1)*batch_size]
        row_batches.append(batch)
    batches.append(row_batches)

# Save batches to directory
for i in range(num_rows):
    for j in range(num_cols):
        cv2.imwrite("batches/batch_" + str(i*num_cols+j+1) + ".jpg", batches[i][j])

# Display batches
for i in range(num_rows):
    for j in range(num_cols):
        cv2.imshow("Batch " + str(i*num_cols+j+1), batches[i][j])

cv2.waitKey(0)
cv2.destroyAllWindows()