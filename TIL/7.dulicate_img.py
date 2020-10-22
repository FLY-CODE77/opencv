import numpy as np
import cv2

img1 = cv2.imread('HappyFish.jpg')
img2 = img1 
img3 = img1.copy()
# same as pyhthon 

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)


# Partial extraction
img4 = img1[40:120,30:150,1]
# this can select ths color too 
img5 = img1[40:120,30:150].copy()
# indexing the parts you want to duplicate 


cv2.imshow('img4',img4)
cv2.imshow('img5',img5)

cv2.waitKey()
cv2.destroyAllWindows()
