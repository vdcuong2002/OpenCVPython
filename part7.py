import cv2
import numpy as np
def empty(a):
    pass
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


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("HueMin","TrackBars", 165, 179, empty)
cv2.createTrackbar("HueMax","TrackBars", 179, 179, empty)
cv2.createTrackbar("SatMin","TrackBars", 17, 255, empty)
cv2.createTrackbar("SatMax","TrackBars", 255, 255, empty)
cv2.createTrackbar("ValMin","TrackBars", 181, 255, empty)
cv2.createTrackbar("ValMax","TrackBars", 255, 255, empty)

img = cv2.imread("Image\card.jpg")
img = cv2.resize(img,(int(img.shape[1]*0.7),int(img.shape[0]*0.7)))

while True:
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("HueMin","TrackBars")
    hmax = cv2.getTrackbarPos("HueMax","TrackBars")
    smin = cv2.getTrackbarPos("SatMin","TrackBars")
    smax = cv2.getTrackbarPos("SatMax","TrackBars")
    vmin = cv2.getTrackbarPos("ValMin","TrackBars")
    vmax = cv2.getTrackbarPos("ValMax","TrackBars")
    print(hmin,hmax,smax,smin,vmax,vmin)
    lower = np.array([hmin,smin,vmin])
    uper = np.array([hmax,smax,vmax])

    mask = cv2.inRange(imgHSV, lower, uper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)


    imgStack = stackImages(0.7,([img, imgHSV],[mask, imgResult]))
    cv2.imshow("OUTPUT", imgStack)

    cv2.waitKey(0)