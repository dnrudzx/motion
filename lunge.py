import numpy as np
import cv2
import math
import keypoint as key
import comphead as cp
import bodyrange as br
import climber as cb

def lunge_waist():
    bNE_x, bNE_y = key.keypoint("blunge", 1)
    bMH_x, bMH_y = key.keypoint("blunge", 8)
    pNE_x, pNE_y = key.keypoint("plunge", 1)
    pMH_x, pMH_y = key.keypoint("plunge", 8)

    bangle = cp.getDegree(bNE_x, bNE_y,bMH_x, bMH_y)
    bwaist= cb.avg(bangle)

    print(bwaist * 1.1)

    pangle = cp.getDegree(pNE_x, pNE_y,pMH_x, pMH_y)

    Ok = []
    false = []
    waist_array = []

    for i in range(len(pangle)):
        print(pangle[i])
        if pangle[i] == 0:
            waist_array.insert(i, " ")
        elif (bwaist * 1.1) < pangle[i]:
            waist_array.insert(i, "허리 각도가 %d입니다. 허리를 펴주세요." % pangle[i])
            false.append(i)
        elif (bwaist * 0.9) > pangle[i]:
            waist_array.insert(i, "허리 각도가 %d입니다. 허리를 펴주세요." % pangle[i])
            false.append(i)
        else:
            waist_array.insert(i, "정상 범위 입니다. ")
            Ok.append(i)

    return Ok, false, waist_array

def isfloor():
    pRK_x, pRK_y = key.keypoint("plunge", 10)
    pLK_x, pLK_y = key.keypoint("plunge", 13)
    pRB_x, pRB_y = key.keypoint("plunge", 19)

    RbY = cb.avg(pRB_y)

    Ok = []
    false = []
    floor_array = []

    for i in range(len(pRK_y)):
        if pRK_y[i] == 0 or pLK_y[i] == 0:
            floor_array.insert(i, " ")
        elif pRK_y[i] < RbY:
            floor_array.insert(i, "오른쪽 무릅을 바닥에 닿게하지 마세요.")
            false.append(i)
        elif pLK_y[i] < RbY:
            floor_array.insert(i, "왼쪽 무릅을 바닥에 닿게하지 마세요.")
            false.append(i)
        else:
            floor_array.insert(i, "정상 범위 입니다. ")
            Ok.append(i)

    return Ok, false, floor_array

def overknee():
    pLK_x, pLK_y = key.keypoint("plunge", 13)
    pRK_x, pRK_y = key.keypoint("plunge", 10)
    pLB_x, pLB_y = key.keypoint("plunge", 19)
    pRB_x, pRB_y = key.keypoint("plunge", 22)

    cm = key.height("plunge")
    print(cm)

    Max_plk, Min_plk = br.Max(pLK_x)
    Max_prk, Min_prk = br.Max(pRK_x)
    Max_plb, Min_plb = br.Max(pLB_x)
    Max_prb, Min_prb = br.Max(pRB_x)

    Rrange = []
    Lrange = []

    for i in range(len(pLB_x)):
        if pLB_x[i] == Min_plb:
            Lrange.append(i)

    for i in range(len(pRB_x)):
        if pRB_x[i] == Min_prb:
            Rrange.append(i)


    L_Ok = []
    L_false = []
    L_over_array = []

    for i in range(len(pLK_x)):
        if pLK_x[i] == 0:
            L_over_array.insert(i, " ")
            if i in Lrange:
                if Min_plb > pLK_x[i]:
                    L_over_array.insert(i, " 왼쪽 무릎이 %fcm 만큼 너무 나아갔습니다." % abs(Min_plb - pLK_x[i])*cm)
                    L_false.append(i)
                else:
                    L_over_array.insert(i, " 왼쪽 무릅을 바닥에 닿게하지 마세요.")
        else:
            L_over_array.insert(i, "정상 범위 입니다. ")
            L_Ok.append(i)

    R_Ok = []
    R_false = []
    R_over_array = []

    for i in range(len(pRK_x)):
        if pRK_x[i] == 0:
            R_over_array.insert(i, " ")
            if i in Rrange:
                if Min_prb > pRK_x[i]:
                    R_over_array.insert(i, "오른쪽 무릎이 %dcm 만큼 너무 나아갔습니다." % abs(Min_prb - pRK_x[i])*cm)
                    R_false.append(i)
                else:
                    R_over_array.insert(i, "오른쪽 무릅을 바닥에 닿게하지 마세요.")
        else:
            R_over_array.insert(i, "정상 범위 입니다. ")
            R_Ok.append(i)

    return R_Ok, L_Ok, L_false, R_false, L_over_array, R_over_array