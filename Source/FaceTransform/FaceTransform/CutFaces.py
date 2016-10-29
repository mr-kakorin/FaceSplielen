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
