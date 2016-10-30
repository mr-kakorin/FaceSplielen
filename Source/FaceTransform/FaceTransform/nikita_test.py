import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np

json='jsonDesc.txt';


cf.getCoordinateFace(json)

img = cv2.imread('kor.jpg');

imgf,fcoord = cf.cutFace('kor.jpg',json);

print(fcoord)
imgf2 = cv2.copyMakeBorder(imgf,0,0,0,0,cv2.BORDER_REPLICATE)

imgg, l, b = cf.rot(imgf,[100,80],31,41,-25,True);

g1,g2,g3 = ft.getFunctionFromMatixWhiteBlack(imgf2,l)

ft.InterpolateBetweenWithRem(imgg,l,g1,g2,g3);
ft.removeEdge(imgg,b);

cv2.imshow('image',imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()



 