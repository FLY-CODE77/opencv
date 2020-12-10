# 언샤프 마스크 필터
import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp',cv2.IMREAD_GRAYSCALE)

if src is None:
    print('no image')
    sys.exit()

blr = cv2.GaussianBlur(src,(0,0),2)
# dst = cv2.addWeighted(src,1, blr,-1,128)
# 공식에 따라서
# dst = cv2.addWeighted(src,2,blr,-1,0)
# 또 다른 방법 clip clip 은 소수점을 표현 해줘야 합니다. float 반환을 해주니깐 형 변환 까찌

dst = np.clip(2.0*src - blr,0,255).astype(np.uint8)


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
