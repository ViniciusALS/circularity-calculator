import cv2
import math


def empty(a):
    pass


cv2.namedWindow('Parameters')
cv2.resizeWindow('Parameters', 600, 200)
cv2.createTrackbar('Threshold1', 'Parameters', 150, 255, empty)
cv2.createTrackbar('Threshold2', 'Parameters', 255, 255, empty)


def getContours(image, imageContours):
    
    _, contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 
    for contour in contours:
        
        cv2.drawContours(imageContours, contours, -1, (255, 0, 0), 3)
        
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = (4 * math.pi * area) / (perimeter * perimeter)
        
        approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)
        
        x, y, w, h = cv2.boundingRect(approx)
        
        cv2.rectangle(imageContours, (x, y), (x+w, y+h), (0,255,0), 1)       
        
        cv2.putText(imageContours, 'Area: ' + str(area), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        cv2.putText(imageContours, 'Perimeter: ' + str(perimeter), (x, y+h+40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        cv2.putText(imageContours, 'Circularity: ' + str(circularity), (x, y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)



image = cv2.imread('hex.png')
imgContour = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


threshold1 = cv2.getTrackbarPos('Threshold1', 'Parameters')
threshold2 = cv2.getTrackbarPos('Threshold2', 'Parameters')

image = cv2.Canny(image, threshold1, threshold2)

getContours(image, imgContour)

cv2.imshow('imgContour', imgContour)


cv2.waitKey()
cv2.destroyAllWindows()