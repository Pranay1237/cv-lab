import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
img = cv2.resize(img, (650, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
_, exp = cv2.threshold(gray, 0, 0, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    cv2.drawContours(img, [approx], 0, (300, 200, 100), 5)
    cv2.drawContours(exp, [approx], 0, (210, 100, 100), 5)

    m = cv2.moments(contour)
    if m['m00'] != 0:
        cx = int(m['m10'] / m['m00']) - 50
        cy = int(m['m01'] / m['m00'])

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Triangle', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    elif len(approx) == 4:
        cv2.putText(img, 'quadrilateral', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'quadrilateral', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Pentagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Hexagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    elif len(approx) == 7:
        cv2.putText(img, 'Heptagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Heptagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    elif len(approx) == 8:
        cv2.putText(img, 'Octagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Octagon', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))
    else :
        cv2.putText(img, 'Circle', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(exp, 'Circle', (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.5, (210, 100, 100))

cv2.imshow('shapes', img)
cv2.imshow('shapes1', exp)
cv2.waitKey(0)
cv2.destroyAllWindows()