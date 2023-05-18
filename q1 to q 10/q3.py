from PIL import Image

# Open input image
input_image = Image.open("Old-Pic.png")

# Print original image information
print("Original image size:", input_image.size)
print("Original image resolution:", input_image.info.get("dpi"))

# Resize image to half the width and height
resized_image = input_image.resize((input_image.size[0] // 2, input_image.size[1] // 2))

# Print resized image information
print("Resized image size:", resized_image.size)
print("Resized image resolution:", resized_image.info.get("dpi"))

# Save resized image
resized_image.save("New-Pic_resized.jpg")