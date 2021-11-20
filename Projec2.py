import cv2
import numpy as np

cap = cv2.VideoCapture(0)

colors = [[21,115,120,179,163,255],
         [0,147,110,6,247,255],
         [73,174,39,156,255,255]]
         #những số này lấy bằng cách trackbar tuef từ từng màu một

colorVal = [[0,162,0]    #brg
            ,[0,0,233]
            ,[223,0,0]]

myPoints = []        #[x,y, colorID]
newPoints = []

def findColor(img, colors, colorVal):

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in colors:
        lower = np.array(color[0:3])
        uper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, uper)
        x,y = getContours(mask)
        cv2.circle(imgResult, (int(x),int(y)), 10, colorVal[count], cv2.FILLED )
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints
    
def getContours(img):
    x,y,h,w = 0,0,0,0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            # print(peri) #Chu vi
            approx = cv2.approxPolyDP(cnt, 0.03*peri, True)
            # print(approx)  #Toa do cac diem canh
            objCol = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w/2, y+h/2

def drawCanvas(myPoints, colorVal):
    for point in myPoints:
        cv2.circle(imgResult, (int(point[0]),int(point[1])), 10, colorVal[point[2]], cv2.FILLED )



while True:
    success, img = cap.read()
    imgResult = img.copy()

    newPoints = findColor(img, colors, colorVal)


    if len(newPoints) != 0 :
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawCanvas(myPoints, colorVal)
    

    cv2.imshow("img", imgResult)

    if  cv2.waitKey(1) & 0xFF == ord('e'):
        break


cap.release()
cv2.destroyAllWindows