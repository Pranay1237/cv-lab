import cv2

# Load the image
img1 = cv2.imread('img1.jpg')

# Convert the image to grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect objects using HOG
boxes, weights = hog.detectMultiScale(gray_img1)

# Draw bounding boxes around the detected objects
for (x, y, w, h) in boxes:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('HOG Detection', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
