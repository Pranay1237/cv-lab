import cv2
import numpy as np

# Load the image
image = cv2.imread('img1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Prewitt filters
prewitt_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
prewitt_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine the x and y gradients
edges = cv2.addWeighted(np.absolute(prewitt_x), 0.5, np.absolute(prewitt_y), 0.5, 0)

# Normalize the edges
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Display the result
cv2.imshow('Prewitt Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
