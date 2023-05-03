#!/usr/bin/env python

from PIL import Image
import os

# Open input image
input_image = Image.open("Old-Pic.png")

# Convert to grayscale
grayscale_image = input_image.convert('L')

# Convert to binary
binary_image = input_image.convert('1')

# Save grayscale image
grayscale_image.save("New-Pic_grayscale.png")

# Save binary image
binary_image.save("New_binary.png")

# Get size of original, grayscale, and binary images
original_size = os.path.getsize("Old-Pic.jpg")
grayscale_size = os.path.getsize("New-Pic_grayscale.png")
binary_size = os.path.getsize("New-Pic_binary.png")

# Print size information
print("Original file size:", original_size, "bytes")
print("Grayscale file size:", grayscale_size, "bytes")
print("Binary file size:", binary_size, "bytes")
print("Grayscale size difference:", original_size - grayscale_size, "bytes")
print("Binary size difference:", original_size - binary_size, "bytes")