# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:53:30 2024

@author: DIVYAM
"""

import numpy as np
import cv2


def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640,240)
cv2.createTrackbar("v1", "Parameters", 0, 255, empty)
cv2.createTrackbar("v2", "Parameters", 255, 255, empty)
cap = cv2.VideoCapture(0)



def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    v1 = cv2.getTrackbarPos("v1", "Parameters")
    v2 = cv2.getTrackbarPos("v2", "Parameters")
    for i, cnt in enumerate(contours): #cnt ek contour he
        area = cv2.contourArea(cnt)
        if (area > 5000) and (hierarchy[0][i][2] < 0 and hierarchy[0][i][3] < 0):
            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [cnt], (255, 255, 255))
            cv2.imshow("Mask",mask)
            avg_color = cv2.mean(imgContour, mask)
        else:
            avg_color = np.array([0,0,0],dtype=np.uint8)
        bgr_array1 = np.array([[avg_color]], dtype=np.uint8) #bgr array   
        hsv_array = cv2.cvtColor(bgr_array1, cv2.COLOR_BGR2HSV) #respective hsv array
        hsv_array[0,0,1] = hsv_array[0,0,1] + 50 #increasing saturation 
        hsv_tuple = tuple(hsv_array[0, 0]) #hsv tuple of pixel
        bgr_array = tuple(bgr_array1[0, 0])
        if (all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_red, upper_red)) or all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_red1, upper_red1))):
            color = "Red " + str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_orange, upper_orange)):
            color = "Orange "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_yellow, upper_yellow)):
            color = "Yellow "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_green, upper_green)):
            color = "Green "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_cyan, upper_cyan)):
            color = "Cyan "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_blue, upper_blue)):
            color = "Blue "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_purple, upper_purple)):
            color = "Purple "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_white, upper_white)):
            color = "White "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_gray, upper_gray)):
            color = "Gray "+ str(bgr_array)
        elif all(lower <= value <= upper for value, lower, upper in zip(hsv_tuple, lower_black, upper_black)):
            color = "Black "+ str(bgr_array)
        else:
            color = str(bgr_array)
            
        if (area > 5000) and (hierarchy[0][i][2] < 0 and hierarchy[0][i][3] < 0):
            cv2.drawContours(imgContour, cnt, -1, (255,0,255),3)
            perim = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perim, True)
            x, y, w, h, = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x+w,y+h),(0,255,0),3)
            cv2.putText(imgContour, "Area: "+ str(int(area)),(x+w-200, y+45), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0),2)
            cv2.putText(imgContour, "Points: "+ str(len(approx)),(x+w-200,y+20),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
            if len(approx) == 4:
                aspectRatio = float(w)/h
                if aspectRatio >= 0.85 and aspectRatio <= 1.15:
                  cv2.putText(imgContour, "Square", (x+w-200, y+70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour, "X and Y: "+str(int((h+w)/2)), (x+w-200, y+95), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour,"Color: "+color, (x+w-200, y+120), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                else:
                  cv2.putText(imgContour, "Rectangle", (x+w-200, y+70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour, "X and Y: "+str(int(w))+" "+str(int(h)), (x+w-200, y+95), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour,"Color: "+color, (x+w-200, y+120), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
            elif len(approx) > 4 and len(approx) <10:
                  cv2.putText(imgContour, "Circle", (x+w-200, y+70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour, "Radius : "+ str(int(h/2)), (x+w-200, y+95), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
                  cv2.putText(imgContour,"Color: "+color, (x+w-200, y+120), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),2)
    
while True:
    success, img = cap.read()
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,100,100])
    upper_red = np.array([9,255,255])
    lower_red1 = np.array([170,100,100])
    upper_red1 = np.array([180,255,255])
    
    lower_orange = np.array([10,100,100])
    upper_orange = np.array([24,255,255])
    
    lower_yellow = np.array([25,100,100])
    upper_yellow = np.array([34,255,255])
    
    lower_green = np.array([35,100,100])
    upper_green = np.array([84,255,255])
    
    lower_cyan = np.array([85,100,100])
    upper_cyan = np.array([114,255,255])
    
    lower_blue = np.array([115,100,100])
    upper_blue = np.array([129,255,255])
    
    lower_purple = np.array([130,100,100])
    upper_purple = np.array([159,255,255])
    
    lower_white = np.array([0,0,210])
    upper_white = np.array([180,30,255])
    
    lower_gray = np.array([0,0,31])
    upper_gray = np.array([180,5,255])
    
    lower_black = np.array([0,0,0])
    upper_black = np.array([180,255,10])
    
        
    imgContour = img.copy()
    blurred = cv2.GaussianBlur(img,(7,7),1)
    grays = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(grays, 64, 26)
    ker = np.ones((5,5))
    dilated = cv2.dilate(canny, ker, iterations=1)
    getContours(dilated, imgContour)
    
    
    cv2.imshow("dileated",dilated)
    cv2.imshow("Real image",img)
    cv2.imshow("canny image",canny)
    cv2.imshow("Contour drawn",imgContour)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    
    
    
    
cap.release()
cv2.destroyAllWindows()