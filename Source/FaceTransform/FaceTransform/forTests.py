import CutFaces as cf
import FaceTransform as ft

testImFace=cf.cutFace('kor.jpg','jsonDesc.txt')
testWB=ft.GetGrayScaleImg(testImFace)
myfun=cf.getFunctionFromMatixWhiteBlack(testWB)
