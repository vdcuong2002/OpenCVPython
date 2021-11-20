import cv2

faceCascade = cv2.CascadeClassifier("Haarsascade/haarcascade_frontalface_default.xml")

img = cv2.imread("Image/Cuongdz.jpg")
img = cv2.resize(img,(int(img.shape[1]*0.1),int(img.shape[0]*0.1)))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow("CuongDZ", img)
cv2.waitKey(0)