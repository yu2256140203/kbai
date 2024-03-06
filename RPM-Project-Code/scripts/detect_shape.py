import cv2
import numpy as np

# Load the image
problem_name = 'Basic Problem D-04'
problem_set = problem_name.split('-')[0].replace('Problem', 'Problems')
image_path = '../Problems/' + problem_set + '/' + problem_name + '/C.png'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# use edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# use thresholding
_, edges = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)


# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(f"Number of contours: {len(contours)}")

# Function to identify shape
def detect_shape(c):
    # Initialize shape name and approximate the contour
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)

    # If the shape is a triangle, it will have 3 vertices
    if len(vertices) == 3:
        shape = "triangle"

    # If the shape has 4 vertices, it is either a square or a rectangle
    elif len(vertices) == 4:
        # Compute the bounding box of the contour and use the
        # bounding box to compute the aspect ratio
        x, y, w, h = cv2.boundingRect(vertices)
        aspect_ratio = w / float(h)

        # A square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if aspect_ratio >= 0.95 and aspect_ratio <= 1.05 else "rectangle"

    # If the shape is a pentagon, it will have 5 vertices
    elif len(vertices) == 5:
        shape = "pentagon"

    elif len(vertices) == 6:
        shape = "hexagon"

    elif len(vertices) == 7:
        shape = "heptagon"

    elif len(vertices) == 8:
        shape = "octagon"
    # Otherwise, we assume the shape is a circle
    else:
        shape = "circle"

    return shape


# Loop through the contours and hierarchy and find contours that are inside others
for i, (contour, hier) in enumerate(zip(contours, hierarchy[0])):
    cv2.drawContours(image, contours, i, (0, 255, 0), 2)
    shape = detect_shape(contour)
    print(f"Shape {i + 1}: {shape}")

# Save the output image with detected shapes
# output_path = '/mnt/data/shapes_detected.png'
# cv2.imwrite(output_path, image)

# If you want to display the image in an interactive window, uncomment the lines below:
cv2.imshow('Detected Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
