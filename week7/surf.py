import cv2

image = cv2.imread('img4.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()

keypoints, descriptors = surf.detectAndCompute(gray, None)

image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, (0, 255, 0), 4)

cv2.imshow('Image with SURF keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
