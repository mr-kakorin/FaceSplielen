import json
import cv2

def cutFace(imageName,jsonDescription):

    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg

def getCoordinateFace(jsonDescrip):
    outListCoordinateFace=[]
    jsLoad=json.load(jsonDescrip)
    for i in [0,2]:
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['y'])
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['x'])
   
    return outListCoordinateFace
