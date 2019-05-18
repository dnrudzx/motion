
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import comphead as head


NO1, NE1 = head.headkeypoints("1")
maxX, maxY = head.Framescale('/home/ms/frame/frame_10.jpg')
x, y = head.NoseKeypoint(NO1, maxX, maxY)
x2, y2 = head.NeckKeypoint(NE1, maxX, maxY)

NO2, NE2 = head.headkeypoints("2")
maxX2, maxY2 = head.Framescale('/home/ms/frame/frame_20.jpg')
x3, y3 = head.NoseKeypoint(NO2, maxX2, maxY2)
x4, y4 = head.NeckKeypoint(NE2, maxX2, maxY2)

def Brange(y, y2, y3, y4):
    


#간단하게 머리 비교하기
def sHead(Angle, Angle2):
    a = Angle
    c = Angle2

    maxA = minA = a[0]

    for i in range(len(a)):
        if a[i] == 0:
            continue
        elif maxA< a[i]:
            maxA = a[i]
        elif minA > a[i]:
            minA = a[i]

    tooH = []
    tooL = []
    ok = []
    count = 0

    for i in c:
        if maxA < i:
            tooL.append(count)
            count += 1
        elif minA > i:
            tooH.append(count)
            count += 1
        else:
            ok.append(count)
            count += 1

    return tooH, tooL, ok

#높은지 낮은지 정상적인지 판단된 프레임을 프린트 해줌
def head_point_out(tooH, tooL, ok):
    allstr = ""
    allarray = []

    count = 0
    for i in range(len(tooH)+len(tooL)+len(ok)):
        path = ('/home/ms/frame/frame_2'+ str(i) +'.jpg')

        print(allstr)
        image = cv2.imread(path)
        cv2.imshow("Moon", image)
        cv2.waitKey(20)
        
        #하나의 문자열로 합치는 과
        if i in tooH:
            allstr += "머리를 너무 높이 들었습니다. 머리를 내려주세요 \n"
        elif i in tooL:
            allstr +="머리를 너무 내렸습니다. 머리를 올려주세요 \n"
        else:
            allstr +="머리 높이가 정확합니다! \n"

    cv2.destroyAllWindows()
    return allstr
