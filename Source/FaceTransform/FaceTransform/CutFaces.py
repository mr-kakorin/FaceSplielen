import FaceTransform as ft
import numpy as np
import json
import cv2
from scipy.interpolate import interp1d
from math import sqrt



def cutFace(imageName,jsonDescription):
    #cutFace return matrix 3-demention cut face from base picture
    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg


def getCoordinateFace(jsonDescrip):
    #getCoordinateFace return list of indexes for slice
    outListCoordinateFace=[];
    with open(jsonDescrip) as jsonfile:
        jsLoad = json.load(jsonfile) 
    for i in [0,2]:
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['y'])
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['x'])     
    return outListCoordinateFace

def getFunctionFromMatixWhiteBlack(img):
    #return func from WB matrix image
    res = cv2.resize(img,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
    vectImg=res.flatten()
    f=interp1d(np.arange(len(vectImg)),vectImg,'cubic')
   
    return f

#listCoord - coordinate of beginning pixel, row, col - rectangle to rotate, iscycle - cycle shape or rec 
def rot(img2,listCoord,row,col, angle,iscycle=False):
    if iscycle==False:
        partIm=img2[listCoord[0]:listCoord[0] + row,listCoord[1]:listCoord[1] + col]
        rows,cols,_ = partIm.shape
        M = cv2.getRotationMatrix2D((cols / 2,rows / 2),30,1)
        dst = cv2.warpAffine(partIm,M,(cols,rows))
        listofindexBlack = []
        for i in range(rows):
            for j in range(cols):
                if dst[i,j].all() == 0:
                    listofindexBlack.append((i + listCoord[0],j + listCoord[1]))
                    img2[i + listCoord[0],j + listCoord[1]] = (img2[i + listCoord[0] - 1,j + listCoord[1]]/2 + img2[i + listCoord[0],j + listCoord[1] - 1]/2)
                else:
                    img2[i + listCoord[0],j + listCoord[1]] = dst[i,j]
    
    else:
        partIm=img2[listCoord[0]:listCoord[0] + row,listCoord[1]:listCoord[1] + row]
        rows,cols=partIm.shape
        M = cv2.getRotationMatrix2D((cols / 2,rows / 2),30,1)
        dst = cv2.warpAffine(partIm,M,(cols,rows))
        listofindexBlack = []
        r=round(rows/2)
        for i in range(rows):
            for j in range(cols):
                if sqrt(float((i-r)**2+(j-r)**2)) > r:
                    listofindexBlack.append((i + listCoord[0],j + listCoord[1]))
                    img2[i + listCoord[0],j + listCoord[1]] = (img2[i + listCoord[0] - 1,j + listCoord[1]] + img2[i + listCoord[0],j + listCoord[1] - 1]) / 2
                else:
                    img2[i + listCoord[0],j + listCoord[1]] = dst[i,j]

    return img2, listofindexBlack


