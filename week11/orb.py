import cv2
# Load the image
image = cv2.imread('img1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create an ORB object
orb = cv2.ORB_create(nfeatures=2000)

# Detect keypoints and compute descriptors
keypoints, descriptors = orb.detectAndCompute(gray, None)

# Draw keypoints on the image with red color
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with keypoints
cv2.imshow("Image with Keypoints", image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
