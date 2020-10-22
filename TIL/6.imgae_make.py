import numpy as np
import cv2

img1 = np.empty((240,320),dtype = np.uint8)
# grayscale 

img2 = np.zeros((240,320,3),dtype = np.uint8)
# color scale
# np.empty == np.zeros 

img3 = np.ones((240,320,3),dtype = np.uint8) * 50
# np.ones() * 255 
img4 = np.full((240,320),128,dtype = np.uint8)
# how to np.full 
# write size and value to fill 
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.waitKey()
cv2.destroyALLWindows()

