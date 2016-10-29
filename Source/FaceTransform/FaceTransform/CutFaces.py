import FaceTransform as ft
import numpy as np
import json
import cv2
from scipy.interpolate import interp1d
from math import sqrt



def cutFace(imageName,jsonDescription):
    #cutFace return matrix 3-demention cut face from base picture
    listCoordFace=getCoordinateFace(jsonDescription)
    img=cv2.imread(imageName)
    cutImg=img[listCoordFace[0]:listCoordFace[2],listCoordFace[1]:listCoordFace[3]]
    return cutImg

CL = [(1 + sqrt(3)) / (4 * sqrt(2)),
(3 + sqrt(3)) / (4 * sqrt(2)),
(3 - sqrt(3)) / (4 * sqrt(2)),
(1 - sqrt(3)) / (4 * sqrt(2))]


def getCoordinateFace(jsonDescrip):
    #getCoordinateFace return list of indexes for slice
    outListCoordinateFace=[];
    with open(jsonDescrip) as jsonfile:
        jsLoad = json.load(jsonfile) 
    for i in [0,2]:
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['y'])
        outListCoordinateFace.append(jsLoad['faceAnnotations'][0]['boundingPoly']['vertices'][i]['x'])     
    return outListCoordinateFace

def getFunctionFromMatixWhiteBlack(img):
    #return func from WB matrix image
    vectImg=img.flatten()

    CH = cf.hpf_coeffs(CL)
    #iCL, iCH = cf.icoeffs(CL, CH)
    Y = cf.pconv(vectImg, CL, CH)
    #X2 = cf.pconv(Y, iCL, iCH, len(CL) - 2)
    print(len(Y))
    
    f=interp1d(np.arange(len(Y)),Y,'cubic')
   
    return f







def icoeffs(CL, CH):
    assert(len(CL) == len(CH))         # Размеры списков коэффициентов должны быть равны
    iCL = []  # Коэффициенты первой строки
    iCH = []  # Коэффициенты второй строки
    for k in range(0, len(CL), 2):
        iCL.extend([CL[k-2], CH[k-2]])
        iCH.extend([CL[k-1], CH[k-1]])
    return (iCL, iCH)
def hpf_coeffs(CL):
    N = len(CL)                    # Количество коэффициентов
    CH = [(-1)**k * CL[N - k - 1]  # Коэффициенты в обратном порядке с чередованием знака
        for k in range(N)]
    return CH
def pconv(data, CL, CH, delta = 0):
    assert(len(CL) == len(CH))         # Размеры списков коэффициентов должны быть равны
    N = len(CL)
    M = len(data)
    out = []                           # Список с результатом, пока пустой
    for k in range(0, M, 2):  # Перебираем числа 0, 2, 4…
        sL = 0                         # Низкочастотный коэффициент
        sH = 0                         # Высокочастотный коэффициент
        for i in range(N):      # Находим сами взвешенные суммы
            sL += data[(k + i - delta) % M] * CL[i]
            sH += data[(k + i - delta) % M] * CH[i]
        out.append(sL)                 # Добавляем коэффициенты в список
        out.append(sH)
    return out


    CH = hpf_coeffs(CL)   # Вычисляем недостающие коэффициенты
    w = image.shape    # Размеры изображения
    imageT = image.copy() # Копируем исходное изображение для преобразования
    for i in range(w[1]):   # Обрабатываем строки
        imageT[i, :] = pconv(imageT[i, :], CL, CH)
    for i in xrange(w):   # Обрабатываем столбцы
        imageT[:, i] = pconv(imageT[:, i], CL, CH)

    # Переупорядочиваем столбцы и строки
    data = imageT.copy()
    data[0:w[1]/2, 0:w/2] = imageT[0:w[1]:2, 0:w:2]
    data[w[1]/2:w[1], 0:w/2] = imageT[1:w[1]:2, 0:w:2]
    data[0:w[1]/2, w/2:w] = imageT[0:w[1]:2, 1:w:2]
    data[w[1]/2:w[1], w/2:w] = imageT[1:w[1]:2, 1:w:2]
    return data

