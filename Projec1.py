import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("Haarsascade/haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("Haarsascade/haarcascade_eye.xml")
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    eyes = eyesCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    
    for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break