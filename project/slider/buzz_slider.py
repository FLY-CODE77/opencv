import os
import cv2
import glob

file_list = os.listdir('.//toy_story')
img_files = [file for file in file_list if file.endswith('.jpg')]
img_files = glob.glob('.//toy_story//*.jpg')

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cnt = len(img_files)
idx = 0
while True:
	img = cv2.imread(img_files[idx])
	if img is None:
		print("no image sir")
		break
	cv2.imshow('image',img)
	if cv2.waitKey(1000) >= 0:
		break
	idx +=1
	if idx >= cnt:
		idx = 0
