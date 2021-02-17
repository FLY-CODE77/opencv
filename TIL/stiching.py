import numpy as np 
import sys
import cv2

img_names = ['img1.jpg', 'img2.jpg', 'img3.jpg']

imgs = []
for name in img_names:
    img = cv2.imread(name)
    
    if img is None :
        print('img load fail')
        sys.exti()
    
    
    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('stitch failed')
    sys.exit()

cv2.imwrite('output.jpg', dst)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()