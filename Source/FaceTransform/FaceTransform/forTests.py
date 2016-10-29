import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt

testCut=cf.cutFace('kor.jpg','jsonDesc.txt')
testWB=ft.GetGrayScaleImg(testCut)
myf=cf.getFunctionFromMatixWhiteBlack(testWB)
#testdw=cf.dwt2(test)
#cv2.imshow('image',testdw)
cv2.waitKey(0)
cv2.destroyAllWindows()