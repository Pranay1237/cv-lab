import cv2

# Read the input image
image = cv2.imread("img3.jpg")

# Adjust the contrast of the image
contrasted_image = cv2.addWeighted(image, 1.5, 0, 0, 0)

# Display the original and contrasted images
cv2.imshow("Original Image", image)
cv2.imshow("Contrasted Image", contrasted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()