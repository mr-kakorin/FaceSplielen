import CutFaces as cf
import FaceTransform as ft
import cv2
from math import sqrt


json='jsonDesc.txt';

tmp = ft.GetMarksCoordinates(json);
print(tmp)