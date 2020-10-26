import cv2
import sys
img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('no image')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image' ,img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord('i') or key == ord('I'):
        img = ~img
        cv2.imshow('image',img)
cv2.destroyAllWindows()
# core 
# if you want some key actions with keyborad
# make key or another name class to save cv2.waitKey() class

