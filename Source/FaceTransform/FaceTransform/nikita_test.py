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

imgg, l = cf.rot(imgf,[100,100],45,62,27);

ft.InterpolateBetween(imgg,l);

cv2.imshow('image',imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()