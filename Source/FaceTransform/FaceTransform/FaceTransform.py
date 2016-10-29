import cv2
import numpy as np
import CutFaces as cf
import json

#convert 3-chaneles image to 1-channel mat summed from 3-channels by mod 255 
def GetTwoDimMatrix(img):
	height, width, channels = img.shape	
	twoDim = np.zeros((height, width,1));
	for i in range(0,height):
		for j in range(0,width):
				twoDim[i,j] = (img[i,j,0])+(img[i,j,1])+(img[i,j,2])
				if twoDim[i,j]>255:
					twoDim[i,j] = twoDim[i,j]-255;
	return twoDim

#get contour from image to use it in find contour area or hull
def GetContour(img):
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray_img,127,255,0)
	_,contours,_ = cv2.findContours(thresh, 1, 2)
	cnt = contours[0]
	return cnt

#get contour area by cont-property from GetContour 
def GetCArea(cnt):
	return cv2.contourArea(cnt)

#get gray scale image from normal image
def GetGrayScaleImg(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

def GetMarksCoordinates(jsonDescrip):
	outListCoordinateFace=[]
	with open(jsonDescrip) as jsonfile:
		jsLoad = json.load(jsonfile)
	for i in range(0,34):
		outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['x'])
		outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['y'])
		#outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['z'])
	return outListCoordinateFace

def TransformMarkCoordinates(markcoord,facecoord):
    for i in range(0,len(markcoord),2):
        markcoord[i] = markcoord[i] - facecoord[1]
        markcoord[i+1] = markcoord[i+1] - facecoord[0]
    return 

def InterpolateBetween(img,ec):
    k=2;
    for i in range(0,len(ec)):
                img[ec[i][0],ec[i][1]] = img[ec[i][0]-k,ec[i][1]]/3+img[ec[i][0],ec[i][1]-k]/3+img[ec[i][0]-k,ec[i][1]-k]/3
                #print(ec[i][0],ec[i][1])      
    for i in range(0,len(ec)):
        if img[ec[i][0],ec[i][1]].any()==0:
            print(ec[i][0],ec[i][1])
    return

def GetIndexesArr(arr):
    h,w,c = img.shape
    resarr=np.array(h,w)
    for i in range(0,h):
        for j in range(0,w):
            resarr.append([i,j]);