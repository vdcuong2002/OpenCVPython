import cv2
import time
import numpy as np
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector  = htm.handDetector(detectionCon=0.7)

pTime = 0
while True:
    __, img = cap.read()
    
    img = detector.findHands(img)

    a = detector.findPosition(img, handNo=0, draw=True)
    
    if (a[0] == 4 or a[0] == 8 ):
        print(a)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255,0), 1 )
    cv2.imshow("img", img)
    cv2.waitKey(1)
