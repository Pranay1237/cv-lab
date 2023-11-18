import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1 = cv2.GaussianBlur(frame, (3, 3), 0)
    frame1 = cv2.Canny(frame, 100, 200)
    cv2.imshow('edge', frame1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

