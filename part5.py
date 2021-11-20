import cv2
import numpy as np

img = cv2.imread("Image/card.jpg")

width = 2.5 * 100
height = 3.5 * 100

pts1 = np.float32([[546,191],[694,226],[460,369],[629,416]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(250,350))

cv2.imshow("Card", img)
cv2.imshow("CardOut", imgOut)

cv2.waitKey(0)