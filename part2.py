import cv2
import numpy as np

img = cv2.imread("Image\Cuongdz.jpg")
img = cv2.resize(img,(int(img.shape[1]*0.1),int(img.shape[0]*0.1)))

ker = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img,200,200)
imgDialation = cv2.dilate(imgCanny,ker, iterations=1)
imgEroded = cv2.erode(imgDialation, ker, iterations=1)

cv2.imshow("CuongDZ", img)
cv2.imshow("Img Gray", imgGray)
cv2.imshow("Img Blur", imgBlur)
cv2.imshow("Img Canny", imgCanny)
cv2.imshow("Img Dialation", imgDialation)
cv2.imshow("Img Eroded", imgEroded)

cv2.waitKey(0)
