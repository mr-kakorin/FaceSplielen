import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np



testCut,tt = cf.cutFace('kor.jpg','jsonDesc.txt')
dic=ft.GetMarksCoordinates('jsonDesc.txt')
ft.TransformMarkCoordinates(dic,tt)
tmp=ft.zalitPart(testCut,dic['RIGHT_EYE'],10,10,dic['NOSE_BOTTOM_CENTER'])

#print(tmp)
#img2 = ft.GetGrayScaleImg(testCut)
rows,cols,_ = testCut.shape
#M = cv2.getRotationMatrix2D((cols / 2,rows / 2), 30,1)
#dst = cv2.warpAffine(testCut,M,(cols,rows))

#img3,t=cf.rot(testCut,[90,80],50,50,30)

#cont=ft.GetContour(img2)
#cont2=ft.GetCArea(cont)

cv2.imshow('image',tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()
#rows,cols = testWB.shape

#center=testWB[100:200,100:200]



#newIm=cf.getIm(y)


#print(res.shape)
