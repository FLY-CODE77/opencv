# python version

import cv2 
import numpy as np
import time

img_color = cv2.imread('chessboard.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('chessboard.jpg', cv2.COLOR_BGR2GRAY)

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_32F,1,0)
img_sobel_y = cv2.Sobel(img_gray, cv2.CV_32F,0,1)

lxlx = img_sobel_x * img_sobel_x
lyly = img_sobel_y * img_sobel_y
lxly = img_sobel_x * img_sobel_y

h, w = img_color.shape[:2]

window_size = 5
offset = int(window_size/2)

r = np.zeros(img_gray.shape)

start = time.perf_counter()
for y in range(offset, h - offset):
    for x in range(offset, w - offset):
        window_lxlx = lxlx[y-offset: y+offset +1 , x-offset : x+offset + 1]
        window_lyly = lyly[y-offset: y+offset +1 , x-offset : x+offset + 1]
        window_lxly = lxly[y-offset: y+offset +1 , x-offset : x+offset + 1]
        

        Mxx = window_lxlx.sum()
        Myy = window_lyly.sum()
        Mxy = window_lxly.sum()

        
        det = Mxx * Myy - Mxy*Mxy
        trace =  Mxx + Myy

        r[y,x] = det - 0.04*(trace **2)
        print(r[y,x])

        
cv2.normalize(r, r, 0.0 , 1.0 , cv2.NORM_MINMAX)

for y in range(offset, h -offset):
    for x in range(offset, w -offset):
        
        if r[y, x][0] > 0.4:
            img_color.itemset((y,x,0), 0)
            img_color.itemset((y,x,1), 0)
            img_color.itemset((y,x,2), 255)

end = time.perf_counter()
print(end - start)

cv2.imshow('original', img_color)
cv2.waitKey()
cv2.destroyAllWindows()