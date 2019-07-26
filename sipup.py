import numpy as np
import cv2
import math
import keypoint as key
import comphead as cp
import bodyrange as br

#목을 너무 기울이지 않는다
def situpNeck():
    bNE_x, bNE_y = key.keypoint("bsitup", 1)
    bNO_x, bNO_y = key.keypoint("bsitup", 0)
    pNE_x, pNE_y = key.keypoint("psitup", 1)
    pNO_x, pNO_y = key.keypoint("bsitup", 0)

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
