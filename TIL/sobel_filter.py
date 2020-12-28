# edge 검출과 미분

# sobel 함수 예제 

import sys
import numpy as np
import cv2

src = cv2.imread('./images/pier_dock_sea_dusk_shore_118549_1920x1080.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('error')
    sys.exit()

kernel = np.array([[-1, 0 , 1], [-2,0,2], [-1,0,1]], dtype = np.float32)

# sobel 안쓰고!
dx = cv2.filter2D(src,-1, kernel, delta = 128)

# sobel 를 사용하면
dy = cv2.Sobel(src, -1,0,1 , delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()