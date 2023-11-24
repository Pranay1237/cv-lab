import cv2
import numpy as np

image = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.Canny(image, 50, 200, None, 3)

cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(cdst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow("Source", image)
cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdst)
cv2.waitKey(0)
cv2.destroyAllWindows()