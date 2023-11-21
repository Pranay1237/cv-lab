import cv2

# Read the input image
image = cv2.imread("img3.jpg", 0)

# Adjust the contrast of the image
contrasted_image = cv2.convertScaleAbs(image, 1.5)

# Display the original and contrasted images
cv2.imshow("Original Image", image)
cv2.imshow("Contrasted Image", contrasted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()