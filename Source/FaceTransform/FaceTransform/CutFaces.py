import FaceTransform as FT
import numpy as np
import json
import cv2
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
#
def cutFaceWB(imageName,jsonDescription):

    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName,0)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg
#cutFace return matrix 3-demention cut face from base picture
def cutFace(imageName,jsonDescription):

    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg
#getCoordinateFace return list of indexes for slice
def getCoordinateFace(jsonDescrip):
    outListCoordinateFace=[]
    jsLoad=json.load(jsonDescrip)
    for i in [0,2]:
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['y'])
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['x'])
   
    return outListCoordinateFace

def getFunction():
    
    tmp=cutFaceWB('kor.jpg',open('jsonDesc.txt','r'))
    vecttmp=tmp.flatten()
    f=interp1d(np.arange(len(vecttmp)),vecttmp)
    #plt.plot(np.arange(len(vecttmp)),vecttmp)
    #plt.show()
    #cv2.imshow('image',tmp)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    pass

