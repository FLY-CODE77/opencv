import numpy as np
import cv2 
filename = 'polygon.bmp'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 5, 3 , 0.04)
dst = cv2.dilate(dst, None)
cv2.imshow('dst', dst)

img[dst > 0.01* dst.max()] = [0,0,255]

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()