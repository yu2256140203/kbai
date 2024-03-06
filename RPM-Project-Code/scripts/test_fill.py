from PIL import Image, ImageDraw
import cv2
import numpy as np

# Load the image
problem_name = 'Basic Problem B-09'
problem_set = problem_name.split('-')[0].replace('Problem', 'Problems')
image_path = '../Problems/' + problem_set + '/' + problem_name + '/C.png'
image = Image.open(image_path)

# Convert the image to grayscale if it's not already in that mode
if image.mode != 'L':
    image = image.convert('L')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Since the shape is a regular octagon and the background is white, we can use the floodfill method.
# We will floodfill from a point just inside the known border of the octagon.
# The border is black (0, 0, 0), so we need a color that is not black or white for the fill.
# We'll start the fill from the center of the image which we expect to be inside the octagon.

# Finding the center of the image
width, height = image.size
center = (int(width/2), int(height/2))

# Color to start the fill (a color that's not black or white)
fill_color = 1  # Almost black but not quite, so it can be replaced later

# Floodfill with almost black starting from the center
ImageDraw.floodfill(image, xy=center, value=fill_color, border=0)

# Replace the almost black fill with pure black
pixels = image.load()
for y in range(height):
    for x in range(width):
        if pixels[x, y] == fill_color:
            pixels[x, y] = 1

# show the result
image.show()

