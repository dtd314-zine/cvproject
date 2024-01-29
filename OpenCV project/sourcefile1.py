# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:49:54 2024

@author: Divyam Kushwah
"""

import cv2 
import numpy as np


img = np.zeros([512,512,3],np.uint8)


img = cv2.line(img, (510,0),(255,255),(255,0,0),10)
img = cv2.rectangle(img,(300,0),(510,100),(255,0,0),14)
img = cv2.circle(img, (300,100),40,(0,255,0),12)

f = cv2.FONT_HERSHEY_TRIPLEX
img = cv2.putText(img, 'FirstprojectDIVYAMTHEDIVINE', (0,250), f, 1, (255,255,0),1,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()