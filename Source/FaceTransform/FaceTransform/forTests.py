import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np

json='jsonDesc.txt';

tmp = ft.GetMarksCoordinates(json);
img = cv2.imread('kor.jpg');
imgf = cf.cutFace('kor.jpg',json);
fcoord = cf.getCoordinateFace(json);
ft.TransformMarkCoordinates(tmp,fcoord);
cutImg=imgf[int(tmp[1]):int(tmp[4])+15,int(tmp[0]):int(tmp[3])];
s1 = range(100,140);
s2 = range(120,260);
l=[];
for i in range(0,40):
    l.append(s1[i])
ft.InterpolateBetween(imgf,l);

cv2.imshow('image',imgf)
cv2.waitKey(0)
cv2.destroyAllWindows()