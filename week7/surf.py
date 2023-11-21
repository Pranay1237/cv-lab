import cv2

# Load the image
image = cv2.imread('img4.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a SURF object
surf = cv2.xfeatures2d.SURF_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = surf.detectAndCompute(gray, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, (0, 255, 0), 4)

# Display the image with keypoints
cv2.imshow('Image with SURF keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
