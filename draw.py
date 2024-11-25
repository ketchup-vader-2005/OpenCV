import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank', blank)
#img = cv.imread('Cat.jpg')
#cv.imshow('Cat', img)

#Turning a part of it red
#blank[300:400, 200:300] = 0, 0, 255

#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
#cv.imshow('rectangle', blank)

#cv.circle(blank, (250,250), 250, (0, 0, 255), thickness=-1)
#cv.imshow('circle', blank)

#cv.line(blank, (0,0), (250,250), (0, 0, 250), thickness=3)
#cv.imshow('line', blank)

cv.putText(blank, 'Hello', (0,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 250), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
