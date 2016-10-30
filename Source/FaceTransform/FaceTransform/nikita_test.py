import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt
import numpy as np

json='jsonDesc.txt';


cf.getCoordinateFace(json)

img = cv2.imread('kor.jpg');

imgf,fcoord = cf.cutFace('kor.jpg',json);

imgf2 = cv2.copyMakeBorder(imgf,0,0,0,0,cv2.BORDER_REPLICATE)

ft.zalitPart(imgf,[100,80],-10,-10,[140,130]);

tmp = ft.GetMarksCoordinates(json);
ft.TransformMarkCoordinates(tmp,fcoord);

for key, values in tmp.items():
	if key == "nose":
		s=values;
		imgg, l, b = cf.rot(imgf,[values[0]-20,values[1]-20],40,50,180,True);

#ft.InterpolateBetween(imgg,v);
g1,g2,g3 = ft.GetThreeChannelstoRem(imgf2,l)





ft.InterpolateBetweenWithRem(imgg,l,g1,g2,g3);

h,w,c = imgg.shape;

for i in range(values[0]-20,values[0]):
	for j in range(values[1]-20,values[1]):
		imgg[i,j] = imgg[i-1,j]/3 + imgg[i,j-1]/3 +imgg[i-1,j-1]/3

ft.removeEdge(imgg,b);

cv2.imshow('image',imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()



 