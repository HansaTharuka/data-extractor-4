# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:41:26 2019

@author: Hansa Tharuka
"""
import sys
import glob
import cv2
icount=0
for img in glob.glob('*.jpg'):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Original image1',image)  
    #cv2.imshow('Original image',gray)
    print(gray.shape[0])
    for i in range(gray.shape[0]):
       for j in range(gray.shape[1]):
           pixel =gray[ i, j]
# =============================================================================
#       if i<0:
#           gray[i,j]=0
# =============================================================================
# =============================================================================
           if (i<210 or i>250):
                gray[i,j]=0
# =============================================================================
           elif (pixel > 150 and pixel<220 ):
                gray[i,j]=255
           
           else:
               gray[i,j]=0
#cv2.imshow('Gray image', gray)
               
    cv2.imwrite('preprocessed'+img+'.jpg',gray)            
#cv2.waitKey(0)
#cv2.destroyAllWindows() 
    
       