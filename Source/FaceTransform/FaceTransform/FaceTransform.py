import cv2
import numpy as np
import CutFaces as cf
import json
import math
from scipy import interpolate
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
	outListCoordinateFace={}
	with open(jsonDescrip) as jsonfile:
		jsLoad = json.load(jsonfile)
	for i in range(0,34):
		outListCoordinateFace[jsLoad['faceAnnotations'][0]['landmarks'][i]['type']]=[
		round(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['y']),
        round(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['x'])]
		#outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['landmarks'][i]['position']['z'])
	return outListCoordinateFace

def zalitPart(img,inlist,row,col,inlistout):
    
    x0=inlist[0]-round(row/2)
    y0=inlist[1]-round(col/2)
    x1=inlistout[0]-round(row/2)
    y1=inlistout[1]-round(col/2)

    for i in range(row):
        for j in range(col):
            img[i+x1,j+y1,:]=img[i+x0,j+y0,:]
    return img

def TransformMarkCoordinates(markcoord,facecoord):
    for i in markcoord.values():
        i[0] = i[0] - facecoord[0]
        i[1] = i[1] - facecoord[1]
    return 

def InterpolateBetween(img,ec):
    k=2;
    for i in range(0,len(ec)):
        img[ec[i][0],ec[i][1]] = img[ec[i][0]-k,ec[i][1]]/3+img[ec[i][0],ec[i][1]-k]/3+img[ec[i][0]-k,ec[i][1]-k]/3
                #print(ec[i][0],ec[i][1])      
    for i in range(0,len(ec)):              
      
           sum =0;
           for j in range(1,9):
               sum = sum + img[ec[i][0]-j,ec[i][1],0]/24 + img[ec[i][0],ec[i][1]-j,0]/24 + img[ec[i][0]-j,ec[i][1]-j,0]/24
           #if sum<30:
                #sum=sum*2#math.log(sum,8);
           #print(sum)
           img[ec[i][0],ec[i][1],0] = sum
        
           sum =0;
           for j in range(1,9):
                sum = sum + img[ec[i][0]-j,ec[i][1],1]/24 + img[ec[i][0],ec[i][1]-j,1]/24 + img[ec[i][0]-j,ec[i][1]-j,1]/24
           #if sum<30:
              # sum=sum*2#math.log(sum,8);
           #print(sum)
           img[ec[i][0],ec[i][1],1] = sum
       
           sum =0;
           for j in range(1,9):
                sum = sum + img[ec[i][0]-j,ec[i][1],2]/24 + img[ec[i][0],ec[i][1]-j,2]/24 + img[ec[i][0]-j,ec[i][1]-j,2]/24
           #if sum<30:
               # sum=sum*2#math.log(sum,8);
                #print(sum)
           img[ec[i][0],ec[i][1],2] = sum        

    return

def InterpolateBetweenWithRem(img,ec,l1,l2,l3):
    k0=[x[0] for x in ec]
    k1=[x[1] for x in ec]
    for i in range(0,len(ec)):     
        img[k0[i],k1[i],0] = l1[i]
        img[k0[i],k1[i],1] = l2[i]
        img[k0[i],k1[i],2] = l3[i]
    return

def sglazh(img,ec):
    h,w,d=img.shape
    k=4
    p=50
    k0=[x[0] for x in ec]
    k1=[x[1] for x in ec]
    for i in range(len(k0)-1):
        if abs(img[ec[i][0],ec[i][1],0]-img[ec[i+1][0],ec[i][1],0])<p or  abs(img[ec[i][0],ec[i][1],0]-img[ec[i][0],ec[i+1][1],0])<p or abs(img[ec[i][0],ec[i][1],0]-img[ec[i+1][0],ec[i+1][1],0])<p: 
            img[ec[i][0],ec[i][1],0] = img[ec[i][0]-k,ec[i][1],0]/3+img[ec[i][0],ec[i][1]-k,0]/3+img[ec[i][0]-k,ec[i][1]-k,0]/3
            
        if abs(img[ec[i][0],ec[i][1],1]-img[ec[i+1][0],ec[i][1],1])<p or  abs(img[ec[i][0],ec[i][1],1]-img[ec[i][0],ec[i+1][1],1])<p or abs(img[ec[i][0],ec[i][1],1]-img[ec[i+1][0],ec[i+1][1],1])<p: 
            img[ec[i][0],ec[i][1],1] = img[ec[i][0]-k,ec[i][1],1]/3+img[ec[i][0],ec[i][1]-k,1]/3+img[ec[i][0]-k,ec[i][1]-k,1]/3
            
        if abs(img[ec[i][0],ec[i][1],2]-img[ec[i+1][0],ec[i][1],2])<p or  abs(img[ec[i][0],ec[i][1],2]-img[ec[i][0],ec[i+1][1],2])<p or abs(img[ec[i][0],ec[i][1],2]-img[ec[i+1][0],ec[i+1][1],2])<p: 
            img[ec[i][0],ec[i][1],2] = img[ec[i][0]-k,ec[i][1],2]/3+img[ec[i][0],ec[i][1]-k,2]/3+img[ec[i][0]-k,ec[i][1]-k,2]/3
            


    return

def GetIndexesArr(arr):
    h,w,c = img.shape
    resarr=np.array(h,w)
    for i in range(0,h):
        for j in range(0,w):
            resarr.append([i,j]);

def getFunctionFromMatixWhiteBlack(img,ec):
    k0=[x[0] for x in ec]
    k1=[x[1] for x in ec]
    l1=[];l2=[];l3=[];
    for i in range(len(ec)):
        l1.append(img[ec[i][0],ec[i][1],0]);   
        l2.append(img[ec[i][0],ec[i][1],1]);   
        l3.append(img[ec[i][0],ec[i][1],2]);    
    return l1,l2,l3;


def removeEdge(img,b):
    tmp = []
    for i in range(len(b)):
        tmp.append(cv2.GaussianBlur(img[b[i][0]:b[i][0]+3,b[i][1]:b[i][1]+3],(5,5),0))
    for i in range(len(b)):
        for j in range(3):
            for e in range(3):
                img[b[i][0]+j,b[i][1]] = tmp[i][j,e];
                img[b[i][0],b[i][1]+j] = tmp[i][j,e];
    return img

def rotel(img,listC,angle,what):

    if what==0:
        return cf.rot(img,[listC[0]-10,listC[1]-10],20,20,angle,True)
    elif what==1:
        return cf.rot(img,[listC[0]-20,listC[1]-20],40,50,angle,True)
    elif what==2:
        return cf.rot(img,[listC[0]-20,listC[1]-20],40,50,angle,True)

