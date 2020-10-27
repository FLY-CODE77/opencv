import cv2
import sys
img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('no img here')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image',img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord('i') or key == ord('I'):
        img = ~img
        cv2.imshow('image',img)
cv2.destroyAllWindows()
