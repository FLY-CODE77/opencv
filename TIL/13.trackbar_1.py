import numpy as np
import cv2
img = np.zeros((480,640),np.uint8)

# np.clip을 활용하면
def on_trackbar(pos):
    global img

    level = pos *16
    level = np.clip(level,0,255)
    # np.clip 범위를 줘 버린다!
    img[:,:] = level
    cv2.imshow('image',img)

# pos?!

cv2.namedWindow('image')
# createabar은 함수가 호출된 후 시작 해야한다

cv2.createTrackbar('level','image',0,16,on_trackbar)

cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows()
