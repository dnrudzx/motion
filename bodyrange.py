import numpy as np
import cv2
import math
import keypoint as key
import comphead as cp

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
            bodyarray.insert(i, "더 내려가 주세요.")
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