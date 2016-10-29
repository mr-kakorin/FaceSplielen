import FaceTransform as ft
import numpy as np
import json
import cv2
from scipy.interpolate import interp1d


def cutFace(imageName,jsonDescription):
    #cutFace return matrix 3-demention cut face from base picture
    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg

def getCoordinateFace(jsonDescrip):
    #getCoordinateFace return list of indexes for slice
    outListCoordinateFace=[]
    jsLoad=json.load(jsonDescrip)
    for i in [0,2]:
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['y'])
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['x'])
   
    return outListCoordinateFace

def getFunctionFromMatixWhiteBlack(img):
    #return func from WB matrix image
    
    vectImg=img.flatten()
    f=interp1d(np.arange(len(vectImg)),vectImg,'cubic')
   
    return f

