import numpy as np
import cv2
import math
import keypoint as key
import comphead as cp
import climber as cb

#최대 값과 최소값을 구해준다
def Max(y):

	maxY = y[0]
	minY = y[0]

	for i in range(len(y)):
		if y[i] == 0:
			continue
		elif y[i] > maxY :
			maxY = y[i]
		elif y[i] < minY :
			minY = y[i]

	return maxY , minY

#기존 동영상의 목 높이와 비교 동영상의 목 높이, 손높이를 넣으면 정상과 낮음을 알려줌
#Ok의 프레임 번호,Low의 프레임 번호, 옳고 틀린지에 대한 문자열 반환
def isbodyrange(y, y2, BminY, PminY):
    b_maxY, b_minY = Max(y)
    p_maxY, p_minY = Max(y2)

    cm = key.height("ppush")

    b_height = b_maxY - BminY
    p_height = p_maxY - PminY

    print(b_height, p_height)
    #원본 동영상 가동 거리와 비교 동영상 가동범위의 높이를 비교해 비슷한 비율로 만듬
    p_rangeMin = p_maxY - (((b_maxY - b_minY) * p_height ) / b_height)

    print(p_rangeMin)
    Ok = []
    Low = []
    bodyarray = []

    for i in range(len(y2)):
        if y2[i] == 0 :
            bodyarray.insert(i, "..")
            continue
        elif y2[i] < p_rangeMin :
            Low.append(i)
            bodyarray.insert(i, "%cm 더 내려가 주세요."%(p_rangeMin - y2[i])*cm)
        else:
            Ok.append(i)
            bodyarray.insert(i, "잘 하고 있습니다.")

    return Ok, Low, bodyarray

#손목 높이를 비교하는데 왼쪽 오른쪽의 값이 더 많은 쪽을 골라서
#골라진 쪽에 어꺠 x, y 손목 x, y 순으로 리턴값을 반환한다
def arm_right_left(num):
    RS_x, RS_y = key.keypoint(num, 2)
    RW_x, RW_y = key.keypoint(num, 4)
    LS_x, LS_y = key.keypoint(num, 5)
    LW_x, LW_y = key.keypoint(num, 6)

    count_left = 0
    count_right = 0

    for i in range(len(RS_x)):
        if RS_x[i] == 0:
            count_right += 1
        elif RS_y[i] == 0:
            count_right += 1
        elif RW_x[i] == 0:
            count_right += 1
        elif RW_y[i] == 0:
            count_right += 1
        elif LS_x[i] == 0:
            count_left += 1
        elif LS_y[i] == 0:
            count_left += 1
        elif LW_x[i] == 0:
            count_left += 1
        elif LW_y[i] == 0:
            count_left += 1
        
    if count_left < count_right :
    	return LS_x, LS_y, LW_x, LW_y
    else :
    	return RS_x, RS_y, RW_x, RW_y

#팔 비교 대상을 구별하기위해 y-10안에 들어오는 프레임값을 반환
#비교할 어깨의 y 값을 넣음
def armframe(p_Y):
    pmaxY = 0

    for i in range(len(p_Y)):
        if pmaxY < p_Y[i]:
            pmaxY = p_Y[i]

    armOb = []
    for i in range(len(p_Y)):
        if (pmaxY - 10) <= p_Y[i]:
            armOb.append(i)

    return armOb

#팔을 폈을떄 수직으로 되있는지 판단한다
#원동 동영상 각도와 비교 동영상 각도, 비교 대상 프레임을 넣어준다
def armheight(Angle, Angle2, armOb):
    
    maxA = 0

    for i in range(len(Angle)):
        if maxA < Angle[i]:
            maxA = Angle[i]

    Ok = []
    Fal = []
    armarray1 = []

    for i in range(len(Angle2)):
        if i in armOb:
            if (maxA * 0.9) > Angle2[i] or (maxA * 1.1) < Angle2[i]:
                armarray1.insert(i, "팔을 수직으로 만들어 주세요.")
                Fal.append(i)
            else:
                armarray1.insert(i, "팔이 수직입니다. ")
                Ok.append(i)
        else:
            armarray1.insert(i, " ")

    return Ok, Fal, armarray1

def dotdist(bNE_x, bNE_y,bMH_x, bMH_y,bLA_x, bLA_y):
	bl_dis = []
	for i in range(len(bNE_x)):
		if bNE_x[i] == 0 or bNE_y[i] == 0 or bMH_x [i]== 0 or bMH_y[i] == 0 or bLA_x[i] == 0 or bLA_y[i] == 0:
			bl_dis.insert(i, 0)
		else:
			area = abs ( (bNE_x[i] - bMH_x[i]) * (bLA_y[i] -  bMH_y[i]) - (bNE_y[i] - bMH_y[i]) * (bLA_x[i] - bMH_x[i]) )
			AB = ( (bNE_x[i] - bLA_x[i]) ** 2 + (bNE_y[i] - bLA_y[i]) ** 2 ) ** 0.5
			bl_dis.insert(i,area/AB)
	return bl_dis

def iswaist():
	bNE_x, bNE_y = key.keypoint("bpush", 1)
	bMH_x, bMH_y = key.keypoint("bpush", 8)
	bRA_x, bRA_y = key.keypoint("bpush", 11)
	bLA_x, bLA_y = key.keypoint("bpush", 14)
	pNE_x, pNE_y = key.keypoint("ppush", 1)
	pMH_x, pMH_y = key.keypoint("ppush", 8)
	pRA_x, pRA_y = key.keypoint("ppush", 11)
	pLA_x, pLA_y = key.keypoint("ppush", 14)

	cm = key.height("ppush")

	br_dis = []
	bl_dis = []
	pr_dis = []
	pl_dis = []

	br_dis = dotdist(bNE_x, bNE_y,bMH_x, bMH_y,bRA_x, bRA_y)
	bl_dis = dotdist(bNE_x, bNE_y,bMH_x, bMH_y,bLA_x, bLA_y)
	pr_dis = dotdist(pNE_x, pNE_y,pMH_x, pMH_y,pRA_x, pRA_y)
	pl_dis = dotdist(pNE_x, pNE_y,pMH_x, pMH_y,pLA_x, pLA_y)

	br_avg = cb.avg(br_dis)
	bl_avg = cb.avg(bl_dis)

	allavg = (br_avg+bl_avg)/2

	y_avg1 = 0
	y_avg2 = 0

	for i in range(len(pNE_y)):
		if pNE_y[i] == 0 or pRA_y[i] == 0:
			continue
		else:
			y_avg1.append((pNE_y[i]+pRA_y[i])/2)

	for i in range(len(pNE_y)):
		if pNE_y[i] == 0 or pLA_y[i] == 0:
			continue
		else:
			y_avg2.append((pNE_y[i]+pLA_y[i])/2)

	y_a = cb.avg(y_avg1)
	y_b = cb.avg(y_avg2)

	all_y = (y_a + y_b)/2

	Ok = []
	Fal = []
	waistarray = []

	for i in range(len(pr_dis)):
		if pr_dis[i] == 0 or pl_dis[i] == 0:
			waistarray.insert(i, " ")
		elif pr_dis[i] == 0 and (allavg * 1.2) < pl_dis[i] and pMH_y>all_y:
			waistarray.insert(i, "허리 각도가 %f입니다. 허리를 펴주세요." % pangle[i])
			false.append(i)
		elif (bwaist * 0.85) > pangle[i]:
			waistarray.insert(i, "허리 각도가 %d입니다. 허리를 펴주세요." % pangle[i])
			false.append(i)
		else:
			waistarray.insert(i, "정상 범위 입니다. ")
			Ok.append(i)

	return Ok, false, waist_array

'''
    maxA = 0
    minA = 0
    for i in range(len(Angle)):
        if Angle[i] > maxA :
            maxA = Angle[i]
        elif Angle[i] < minA :
            minA = Angle[i]
    
    Ok = []
    Fal = []
    armarray = []

    for i in range(len(Angle2)):
        if Angle2 == 0:
            continue
        elif maxA > Angle2[i] and minA < Angle2[i]:
            Ok.append(i)
            armarray.insert(i, "정상입니다.")
        else:
            Fal.append(i)
            armarray.insert(i, "어깨와 손목을 수직으로 만들어 주세요.")

    return Ok, Fal, armarray
'''