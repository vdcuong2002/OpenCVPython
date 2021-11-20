import cv2
import numpy as np
import math

BLACK = (0,0,0) 

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContours, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            # print(peri) #Chu vi
            approx = cv2.approxPolyDP(cnt, 0.03*peri, True)
            # print(approx)  #Toa do cac diem canh
            objCol = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours, (x,y), (x+w,y+h), BLACK, 2 )
            objType = "None"
            if objCol == 3:  objType = "Tam giac"
            elif objCol == 4:
                checkSquare = (peri/4)/(math.sqrt(area))
                if 0.95<checkSquare<1.05: objType = "Hinh vuong"
                else :objType = "Hinh chu nhat"
            else: objType="Hinh tron"

            cv2.putText(imgContours, objType, (x,int(y+h/2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, BLACK,2)


img = cv2.imread("Image\shape.png")

imgContours = img.copy()
a= img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow("Anh goc", img)
cv2.imshow("Output", imgContours)

cv2.waitKey(0)