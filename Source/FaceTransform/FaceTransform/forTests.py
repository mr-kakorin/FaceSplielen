import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np


testCut = cf.cutFace('kor.jpg','jsonDesc.txt')
img2 = ft.GetGrayScaleImg(testCut)



rot(img2,[200,150],30,30,45,True)

#cv2.imshow('res',img1)
#rows,cols = testWB.shape

#center=testWB[100:200,100:200]



#newIm=cf.getIm(y)


#print(res.shape)
