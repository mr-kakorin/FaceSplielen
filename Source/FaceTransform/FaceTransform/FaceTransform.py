import cv2
import numpy as np
from matplotlib import pyplot as plt
import CutFaces as CF

def GetThreeDimMatrix(img):
	height, width, channels = img.shape	
	twoDim = np.zeros((height, width,1), dtype='int64');
	for i in range(0,height):
		for j in range(0,width):
				twoDim[i,j] = int(img[i,j,0])+int(img[i,j,1])+int(img[i,j,2])
				if twoDim[i,j]>255:
					twoDim[i,j] = twoDim[i,j]-255;
	return twoDim

def GetContour(img):
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray_img,127,255,0)
	_,contours,_ = cv2.findContours(thresh, 1, 2)
	cnt = contours[0]
	return cnt

def GetCArea(cnt):
	return cv2.contourArea(cnt)

print(GetThreeDimMatrix(cv2.imread('test.jpg')));

