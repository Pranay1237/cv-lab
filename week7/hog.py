
import cv2

# Load the image
img1 = cv2.imread('img1.jpg')

# Convert the image to grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Initialize the HOG descriptor
hog = cv2.HOGDescriptor()

# Compute the HOG features for the image
hog_features = hog.compute(gray_img1)

# Print the HOG features
print(hog_features)
