import numpy as np
import cv2
import math
import keypoint as key
import comphead as cp
import bodyrange as br

#평균값을 구함 0은 제외한다
def avg(x):
    num = 0
    result = 0
    for val in x:
        if val != 0:
            result += val
            num += 1
    return result/num
#무릅의 비교할 프레임을 구한다
def Kneeframe(PX):
    pminX = 0

    for i in range(len(PX)):
        if pminX < PX[i]:
            pminX = PX[i]

    armOb = []
    for i in range(len(PX)):
        if (pminX + 10) >= PX[i]:
            KneeOb.append(i)

    return KneeOb

#기존 동영상의 무릅 x축의 최대값과 최소값을 구한뒤
#그 값을 가지고 가동범위를 구함 
def ispullknee():
    bRK_x, bRK_y = key.keypoint(bsitup, 10)
    bLK_x, bLK_y = key.keypoint(bsitup, 13)
    bMH_x, bMH_y = key.keypoint(bsitup, 8)
    bNE_x, bNE_y = key.keypoint(bsitup, 1)
    pRK_x, pRK_y = key.keypoint(psitup, 10)
    pLK_x, pLK_y = key.keypoint(psitup, 13)
    pMH_x, pMH_y = key.keypoint(psitup, 8)
    pNE_x, pNE_y = key.keypoint(psitup, 1)
    b_maxRX, b_minRX = br.Max(bRK_x)
    b_maxLX, b_minLX = br.Max(bLK_x)
    p_maxRX, p_minRX = br.Max(pRK_x)
    p_maxLX, p_minLX = br.Max(pLK_x)

    count = 0
    
    bMH = avg(bMH_x)
    pMH = avg(pMH_x)
    bNE = avg(bNE_x)
    pNE = avg(pNE_x)

    bRratio = (bMH - b_minRX)/(bMH - bNE) * 100
    bLratio = (bMH - b_minLX)/(bMH - bNE) * 100

    pRratio = (pMH - pNE) * bRratio
    pLratio = (pMH - pNE) * bLratio

    if bRratio < bLratio :
        if pRratio > pLratio :
            temp = pRratio
            pRratio = pLratio
            pLratio = pRratio

    pRKOB = Kneeframe(pRK_x)
    pLKOB = Kneeframe(pLK_x)

    Ok = []
    false = []
    Kneearray = []

    for i in range(len(pRK_x)):
        if i in pRKOB:
            if (pRratio * 0.9) > pRK_x[i]:
                Kneearray.insert(i, "무릅을 %d 만큼 너무 많이 당겼습니다." % ((pRratio) - pRK_x[i]))
                false.append(i)
            elif (pRratio * 1.1) < pRK_x[i]:
                Kneearray.insert(i, "무릅을 %d 만큼 더 당겨주세요." % (pRK_x[i] - (pRratio)))
                false.append(i)
            else:
                Kneearray.insert(i, "정상 범위 입니다. ")
                Ok.append(i)
        else:
            Kneearray.insert(i, " ")
    return OK, false, Kneearray


def C_armheight(Angle, Angle2):
    
    maxA = 0

    for i in range(len(Angle)):
        if maxA < Angle[i]:
            maxA = Angle[i]

    Ok = []
    Fal = []
    Carmarray = []

    for i in range(len(Angle2)):
        if (maxA * 0.9) > Angle2[i] or (maxA * 1.1) < Angle2[i]:
            Carmarray.insert(i, "팔을 수직으로 만들어 주세요.")
            Fal.append(i)
        else:
            Carmarray.insert(i, "팔이 수직입니다. ")
            Ok.append(i)

    return Ok, Fal, Carmarray

def Hipheight():
    bMH_x, bMH_y = key.keypoint(bsitup, 8)
    pMH_x, pMH_y = key.keypoint(psitup, 8)

    bHip = avg(bMH_y)

    Ok = []
    Fal = []
    array = []

    for i in range(len(pMH_y)):
        if (bHip * 0.9) > pMH_y[i]:
            array.insert(i, "엉덩이가 %d 만큼 낮습니다."% ((bHip) - pMH_y[i])
            Fal.append(i)
        elif (bHip * 1.1) < pMH_y[i]:
            array.insert(i, "엉덩이가 %d 만큼 높습니다."% (pMH_y[i] - (bHip)))
            Fal.append(i)
        else:
            array.insert(i, "정상 범위 입니다. ")
            Ok.append(i)

    return OK,Fal,array