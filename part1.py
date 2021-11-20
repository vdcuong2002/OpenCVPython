import cv2
img = cv2.imread("Image\Cuongdz.jpg")
img = cv2.resize(img,(int(img.shape[1]*0.1),int(img.shape[0]*0.1)))

cv2.imshow("CuongDZ", img)
cv2.waitKey(0)