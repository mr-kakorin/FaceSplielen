import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt


json='jsonDesc.txt';

tmp = ft.GetMarksCoordinates(json);
img = cv2.imread('kor.jpg');
imgf = cf.cutFace('kor.jpg',json);
cutImg=imgf[int(tmp[1]):int(tmp[4]),int(tmp[0]):int(tmp[3])];

