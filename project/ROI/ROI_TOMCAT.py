
import cv2
import numpy as np
import matplotlib.pylab as plt 

img = cv2.imread("/Users/codefreak/code/git/opencv/project/ROi/data/F-14_real.jpg",cv2.IMREAD_COLOR)

# 마스크 영상은 0이 아닌곳에서만 동작한다 

# 라인을 따고 라인 밖은 0 으로 만들어 주자
# image 컨투어 부터 하자