import cv2

img = cv2.imread("Image/Cuongdz.jpg")
img = cv2.resize(img, (int(img.shape[1]/10), int(img.shape[0]/10)))

imgCroped = img[0:100,300:300]

cv2.imshow("Normal", img)
cv2.imshow("Img Croped", imgCroped)


cv2.waitKey(0)