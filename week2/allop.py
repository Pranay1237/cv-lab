import cv2

img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

sumres = cv2.sumElems(img1)
mean, stddev = cv2.meanStdDev(img1)
minv, maxv, minloc, maxloc = cv2.minMaxLoc(img2)

print(f"sum of the elements :  {sumres}")
print(f"mean : {mean}")
print(f"standard deviation : {stddev}")
print(f"minimum value : {minv}")
print(f"maximum value : {maxv}")
print(f"minimum value location : {minloc}")
print(f"maximum value location : {maxloc}")