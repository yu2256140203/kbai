import cv2
import numpy as np

# Load the image
problem_name = 'Basic Problem B-10'
problem_set = problem_name.split('-')[0].replace('Problem', 'Problems')
image_path = '../Problems/' + problem_set + '/' + problem_name + '/B.png'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection as needed
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blurred, 50, 150)
# _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assume the first contour is the target shape; adjust as necessary
# Fill the shape with white
cv2.drawContours(gray, contours, 0, 255, thickness=cv2.FILLED)

# Save or show the result
cv2.imshow('tmp', gray)  # Or display the result
cv2.waitKey(0)
cv2.destroyAllWindows()
