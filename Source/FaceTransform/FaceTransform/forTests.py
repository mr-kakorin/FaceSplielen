import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np


testCut = cf.cutFace('kor.jpg','jsonDesc.txt')
img2 = ft.GetGrayScaleImg(testCut)
img3,t=cf.rot(testCut,[50,100],50,50,30)

#cont=ft.GetContour(img2)
#cont2=ft.GetCArea(cont)

cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#rows,cols = testWB.shape

#center=testWB[100:200,100:200]



#newIm=cf.getIm(y)


#print(res.shape)
