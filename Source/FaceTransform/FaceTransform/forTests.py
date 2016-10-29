import CutFaces as cf
import FaceTransform as ft
import matplotlib.pyplot as plt
#testImFace=cf.cutFace('kor.jpg','jsonDesc.txt')
#testWB=ft.GetGrayScaleImg(testImFace)
#myfun=cf.getFunctionFromMatixWhiteBlack(testWB)


x = linspace(0, 5, 10)
y = x ** 2
plt.figure()
plt.plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
plt.show()