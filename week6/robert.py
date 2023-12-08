import cv2
import numpy as np

# Load an image
image = cv2.imread('path/to/image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Robert edge detection kernels
kernel_x = np.array([[1, 0], [0, -1]])
kernel_y = np.array([[0, 1], [-1, 0]])

robert_x = cv2.filter2D(gray, -1, kernel_x)
robert_y = cv2.filter2D(gray, -1, kernel_y)

# Compute the magnitude of the gradients
magnitude = np.sqrt(robert_x**2 + robert_y**2)

# Normalize the magnitude to the range [0, 255]
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the result
cv2.imshow('Robert Edge Detector', magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
