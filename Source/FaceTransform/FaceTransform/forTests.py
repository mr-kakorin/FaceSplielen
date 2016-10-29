import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt

testCut=cf.cutFace('kor.jpg','jsonDesc.txt')
testWB=ft.GetGrayScaleImg(testCut)

res = cv2.resize(testWB,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
unres=cv2.resize(res,None,fx=10, fy=10, interpolation = cv2.INTER_CUBIC)
cf.getFunctionFromMatixWhiteBlack(testWB)
#print(res.shape)
cv2.imshow('image',unres)
cv2.waitKey(0)
cv2.destroyAllWindows()