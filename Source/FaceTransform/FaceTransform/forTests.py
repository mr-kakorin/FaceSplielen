import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np

testCut = cf.cutFace('kor.jpg','jsonDesc.txt')
img2 = ft.GetGrayScaleImg(testCut)

def rot(img2,listCoord,row,col, angle,iscycle=False):
    if iscycle==False:
        partIm=img2[listCoord[0]:listCoord[0] + row,listCoord[1]:listCoord[1] + col]
        rows,cols=partIm.shape
        M = cv2.getRotationMatrix2D((cols / 2,rows / 2),30,1)
        dst = cv2.warpAffine(partIm,M,(cols,rows))
        listofindexBlack = []
        for i in range(rows):
            for j in range(cols):
                if dst[i,j] == 0:
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


rot(img2,[200,150],30,30,45,True)

#cv2.imshow('res',img1)
#rows,cols = testWB.shape

#center=testWB[100:200,100:200]



#newIm=cf.getIm(y)


#print(res.shape)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()