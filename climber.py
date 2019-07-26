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

    return (result/num)
#무릅의 비교할 프레임을 구한다
def Kneeframe(PX):
    pminX = PX[0]
    KneeOb = []
    MaxY = 0

    for i in range(len(PX)):
    	if PX[i] == 0:
    		continue
    	elif pminX > PX[i]:
    		pminX = PX[i]

    armOb = []
    for i in range(len(PX)):
    	if PX[i] == 0 or i < MaxY:
    		continue
    	elif (pminX * 0.5) < PX[i] and (pminX * 1.5) > PX[i]:
    		for j in range(i, len(PX)):
    			if PX[j] <= PX[j+1]:
    				MaxY = j
    				KneeOb.append(j)
    				break
    print(KneeOb)
    return KneeOb

#
def maxframe():
	pminX = PX
#기존 동영상의 무릅 x축의 최대값과 최소값을 구한뒤
#그 값을 가지고 가동범위를 구함 
def ispullknee():
    bRK_x, bRK_y = key.keypoint("bclimber", 10)
    bLK_x, bLK_y = key.keypoint("bclimber", 13)
    bMH_x, bMH_y = key.keypoint("bclimber", 8)
    bNE_x, bNE_y = key.keypoint("bclimber", 1)
    pRK_x, pRK_y = key.keypoint("pclimber", 10)
    pLK_x, pLK_y = key.keypoint("pclimber", 13)
    pMH_x, pMH_y = key.keypoint("pclimber", 8)
    pNE_x, pNE_y = key.keypoint("pclimber", 1)
    b_maxRX, b_minRX = br.Max(bRK_x)
    b_maxLX, b_minLX = br.Max(bLK_x)
    p_maxRX, p_minRX = br.Max(pRK_x)
    p_maxLX, p_minLX = br.Max(pLK_x)
    
    bMH = avg(bMH_x)
    pMH = avg(pMH_x)
    bNE = avg(bNE_x)
    pNE = avg(pNE_x)


    bRratio = (bMH - b_minRX)/(bMH - bNE)
    bLratio = (bMH - b_minLX)/(bMH - bNE)

    pRratio = pMH - ((pMH - pNE) * bRratio)
    pLratio = pMH - ((pMH - pNE) * bLratio)
    
    if bRratio < bLratio :
        if pRratio > pLratio :
            temp = pRratio
            pRratio = pLratio
            pLratio = pRratio

    pRKOB = Kneeframe(pRK_x)
    pLKOB = Kneeframe(pLK_x)

    Ok = []
    false = []
    RKneearray = []

    for i in range(len(pRK_x)):
    	if pRK_x[i] == 0:
    		RKneearray.insert(i, " ")
    	if i in pRKOB:
    		if (pRratio * 0.9) > pRK_x[i]:
    			RKneearray.insert(i, "무릅을 %d 만큼 너무 많이 당겼습니다." % ((pRratio) - pRK_x[i]))
    			false.append(i)
    		elif (pRratio * 1.1) < pRK_x[i]:
    			RKneearray.insert(i, "무릅을 %d 만큼 더 당겨주세요." % (pRK_x[i] - (pRratio)))
    			false.append(i)
    		else:
    			RKneearray.insert(i, "정상 범위 입니다. ")
    			Ok.append(i)
    	else:
    		RKneearray.insert(i, " ")

    for i in range(len(pLK_x)):
    	if pRK_x[i] == 0:
    		RKneearray.insert(i, " ")
    	if i in pLKOB:
    		if (pLratio * 0.9) > pLK_x[i]:
    			RKneearray.insert(i, "무릅을 %d 만큼 너무 많이 당겼습니다." % ((pRratio) - pRK_x[i]))
    			false.append(i)
    		elif (pLratio * 1.1) < pLK_x[i]:
    			RKneearray.insert(i, "무릅을 %d 만큼 더 당겨주세요." % (pRK_x[i] - (pRratio)))
    			false.append(i)
    		else:
    			RKneearray.insert(i, "정상 범위 입니다. ")
    			Ok.append(i)
    	else:
    		RKneearray.insert(i, " ")

    return Ok, false, RKneearray


def C_armheight(Angle, Angle2):
    avgA = avg(Angle)

    Ok = []
    Fal = []
    Carmarray = []

    for i in range(len(Angle2)):
        if Angle2[0] == 0:
        	Carmarray.insert(i, " ")
        	Fal.append(i)
        elif (avgA * 0.9) > Angle2[i] or (avgA * 1.1) < Angle2[i]:
            Carmarray.insert(i, "팔을 수직으로 만들어 주세요.")
            Fal.append(i)
        else:
            Carmarray.insert(i, "팔이 수직입니다. ")
            Ok.append(i)

    return Ok, Fal, Carmarray

def Hipheight():
    bMH_x, bMH_y = key.keypoint("bclimber", 8)
    bNE_x, bNE_y = key.keypoint("bclimber", 1)
    pMH_x, pMH_y = key.keypoint("pclimber", 8)
    pNE_x, pNE_y = key.keypoint("pclimber", 1)

    bHip = avg(bMH_y)
    pHip = avg(pMH_y)
    bmaxY, bminY = br.Max(bMH_y)

    maxcha = bmaxY - bHip
    mincha = bHip - bminY 
    
    bangle = cp.getDegree(bNE_x, bNE_y, bMH_x, bMH_y)
    pangle = cp.getDegree(pNE_x, pNE_y, pMH_x, pMH_y)
    
    bwaist = avg(bangle)
    pwaist = avg(pangle)

   
    
    ph /=count
    Ok = []
    Fal = []
    array = []

    cou = 0
    for i in range(len(pMH_y)):
    	if pMH_y[i] == 0:
    		array.insert(i, "")
    	elif(ph - mincha) > pMH_y[i]:
    		array.insert(i, "엉덩이가 %d 만큼 낮습니다."% ((ph - mincha) - pMH_y[i]))
    		Fal.append(i)
    	elif (ph + maxcha) < pMH_y[i]:
    		array.insert(i, "엉덩이가 %d 만큼 높습니다."% (pMH_y[i] - (ph + mincha)))
    		Fal.append(i)
    	else:
    		array.insert(i, "정상 범위 입니다. ")
    		Ok.append(i)

    return Ok,Fal,array