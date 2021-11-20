import cv2
import numpy as np

BLUE = (255,0,0)

img = np.zeros((512,512,3),np.uint8)
# img[:] = 255,0,0

cv2.line(img,(0,0),(100,100), BLUE, 2)
cv2.rectangle(img,(0,0),(100,100),BLUE,2)
cv2.circle(img,(100,100),50,BLUE,2)
cv2.putText(img,"CuongDZ",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,BLUE,1)


cv2.imshow("Img", img)

cv2.waitKey(0)