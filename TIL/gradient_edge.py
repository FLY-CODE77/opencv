# edge 검출 with gradient 크기를 사용 

import sys
import numpy as np
import cv2

src = cv2.imread('HappyFish.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('error')
    sys.exit()

kernel = np.array([[-1, 0 , 1], [-2,0,2], [-1,0,1]], dtype = np.float32)

# sobel 안쓰고!
dx = cv2.filter2D(src, cv2.CV_32F, kernel )

# sobel 를 사용하면
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1 )

# 그라이디언트 크기 계산 float 값 인자들을 받아서! float 형으로 변환 시켜준다  
mag = cv2.magnitude(dx,dy)

# 크기는 255 보다 커질수 있으니깐.. clip 을 시킨다 
mag = np.clip(mag,0,255).astype(np.uint8)


edge = np.zeros(mag.shape[:2], np.uint8)
# 여기서 >120 이란 값을 잘 조절하면서 하면 찾고자 하는 형태의 엣지 값을 파악 가능하다
edge[mag> 120] = 255

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge)

cv2.waitKey()

cv2.destroyAllWindows()