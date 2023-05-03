#!/usr/bin/env python

from PIL import Image
import os

# Set file paths for input and output directories
# this way :
# input_dir = "/path/to/input/directory"
# output_dir = "/path/to/output/directory"

input_dir = "/home/mohamed/0x01-Image_processing/images/old-pic"
in_filename ="Old-Pic.png"
output_dir = "/home/mohamed/0x01-Image_processing/images/new-pic"
out1_filename ="NewPic_1.jpg"
out2_filename ="NewPic_2.png"


# Open image file from input directory
image = Image.open(os.path.join(input_dir, in_filename))

# Save image in output directory with new filename and extension
image.save(os.path.join(output_dir, out1_filename))
image.save(os.path.join(output_dir, out2_filename))


# Get size of original and converted image files
original_size = os.path.getsize(os.path.join(input_dir, in_filename))
converted_size = os.path.getsize(os.path.join(output_dir, out1_filename))
converted_size = os.path.getsize(os.path.join(output_dir, out1_filename))

# Print size information
print("Original file size:", original_size, "bytes")
print("Converted file size:", converted_size, "bytes")
print("Size difference:", original_size - converted_size, "bytes")