from PIL import Image

# Open input image
input_image = Image.open("Old-Pic.png")

# Split image into R, G, B channels
r_channel, g_channel, b_channel = input_image.split()

# Display R, G, B channels
r_channel.show()
g_channel.show()
b_channel.show()

# Convert R, G, B channels to grayscale
r_grayscale = r_channel.convert('L')
g_grayscale = g_channel.convert('L')
b_grayscale = b_channel.convert('L')

# Save R, G, B grayscale channels
r_grayscale.save("New_r_grayscale.png")
g_grayscale.save("New_g_grayscale.png")
b_grayscale.save("New_b_grayscale.png")