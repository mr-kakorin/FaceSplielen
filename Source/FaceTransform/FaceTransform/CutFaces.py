import FaceTransform as FT
import json
import cv2

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
