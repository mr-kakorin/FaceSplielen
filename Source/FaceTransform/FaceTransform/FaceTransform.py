import cv2
import numpy as np
import CutFaces as cf
import json
import math
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
    
    if img.ndim>2:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray_img=img
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
        if img[ec[i][0],ec[i][1],0]<50:
           sum =0;
           for j in range(1,9):
               sum = sum + img[ec[i][0]-j,ec[i][1],0]/24 + img[ec[i][0],ec[i][1]-j,0]/24 + img[ec[i][0]-j,ec[i][1]-j,0]/24
           if sum<60:
                sum=sum*math.log(sum,2);
           #print(sum)
           img[ec[i][0],ec[i][1],0]= sum
        if img[ec[i][0],ec[i][1],1]<50:
           sum =0;
           for j in range(1,9):
                sum = sum + img[ec[i][0]-j,ec[i][1],1]/24 + img[ec[i][0],ec[i][1]-j,1]/24 + img[ec[i][0]-j,ec[i][1]-j,1]/24
           if sum<60:
               sum=sum*math.log(sum,2);
           #print(sum)
           img[ec[i][0],ec[i][1],1]= sum
        if img[ec[i][0],ec[i][1],2]<50:
           sum =0;
           for j in range(1,9):
                sum = sum + img[ec[i][0]-j,ec[i][1],2]/24 + img[ec[i][0],ec[i][1]-j,2]/24 + img[ec[i][0]-j,ec[i][1]-j,2]/24
           if sum<60:
                sum=sum*math.log(sum,2);
                #print(sum)
           img[ec[i][0],ec[i][1],2]= sum
        print(img[ec[i][0],ec[i][1]])

    return

def InterpolateBetween2(img,ec):
    k=2;
    for i in range(0,len(ec)):
        img[ec[i][0],ec[i][1]] = img[120,120]#img[ec[i][0]-k,ec[i][1]]/3+img[ec[i][0],ec[i][1]-k]/3+img[ec[i][0]-k,ec[i][1]-k]/3
                #print(ec[i][0],ec[i][1])      
   

    return

def sglazh(img):
    h,w,d=img.shape
    k=2
    p=50
    for i in range(h):
        for j in range(w):
            if abs(img[i,j,0] - img[i-1,j,0])>p and abs(img[i,j,0] - img[i,j-1,0])> p and abs(img[i,j,0] - img[i-1,j-1,0])> p:
                img[i,j,0] = img[i-k,j,0]/3+img[i,j-k,0]/3+img[i-k,j-k,0]/3
            if abs(img[i,j,1] - img[i-1,j,1])>p and abs(img[i,j,1] - img[i,j-1,1])>p and abs(img[i,j,1] - img[i-1,j-1,1])>p:
                img[i,j,1] = img[i-k,j,1]/3+img[i,j-k,1]/3+img[i-k,j-k,1]/3
            if abs(img[i,j,2] - img[i-1,j,2])>p and abs(img[i,j,2] - img[i,j-1,2])>p and abs(img[i,j,2] - img[i-1,j-1,2])>p:
                img[i,j,2] = img[i-k,j,2]/3+img[i,j-k,2]/3+img[i-k,j-k,2]/3

    return

def GetIndexesArr(arr):
    h,w,c = img.shape
    resarr=np.array(h,w)
    for i in range(0,h):
        for j in range(0,w):
            resarr.append([i,j]);