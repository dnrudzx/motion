import keypoint as kp
import numpy as np
import bodyrange as br
import cv2
import math


#목의 높이를 받아와 두영상이 비슷한지 확인한다.
#y1은 비교 동영상, y2는 비교할 동영상
def same(y1, y2):
    
    Ymax1, Ymin1 = br.Max(y1)
    Ymax2, Ymin2 = br.Max(y2)

    result = []
    # for i in range(len(y2)):
    #     result.append(((y2[i]/Ymax2) *100))
    # return result
    # for i in range(len(y1)):
    #     result.append(((y1[i]/Ymax1) *100))
    # return result

    result = {}
    for i in range(len(y2)):
        if y2[i] == 0 :
            result[i] = 0
            continue
        else :
            y2per = ((y2[i]/Ymax2) *100)

            for x in range(len(y1)):
                if y1[x] == 0:
                    continue
                y1per = ((y1[x]/Ymax1) *100)
                if (y2per * 1.2) > y1per and (y2per * 0.8) < y1per :
                    result[i] = x
                    break

    return result
'''
#
def Framescale(filename):
    image = cv2.imread(filename)
    
    height, width, channel = image.shape
    
    return width, height

#코와 목의 키포인트를 프레임숫자에 맞춰서 배열로 만들어줌

def headkeypoints(num):
    NO = np.zeros((1,3))
    NE = np.zeros((1,3))

    count = 0

    while True:
        try:
            a = np.load("../test/array_"+ num +"%d.npy"% count)
        except FileNotFoundError:
            break
    
        if count == 0:
            NO[0, 0] = a[0, 0, 0]   
            NO[0, 1] = a[0, 0, 1]
            NO[0, 2] = a[0, 0, 2]
            NE[0, 0] = a[0, 1, 0]
            NE[0, 1] = a[0, 1, 1]
            NE[0, 2] = a[0, 1, 2]

        else:
            try:
                NO = np.insert(NO, count, a[0, 0], axis=0)        
                NE = np.insert(NE, count, a[0, 1], axis=0)
            except IndexError:
                NO = np.insert(NO, count, 0, axis=0)        
                NE = np.insert(NE, count, 0, axis=0)
        count += 1

    return NO, NE


#push3R.avi


def NoseKeypoint(NO, maxX, maxY):
    #코 배열을 가져와 x값을 x배열에 넣는다
    #값이 0 이면 0을 넣어주고 x값이 가로 크기/2 보다 크면 머리가 왼쪽으로 오게 바꿔준다
    x = []
    for i in range(0, len(NO)):
        if NO[i,0] == 0:
            x = np.insert(x, i, 0)
            continue
        elif (maxX/2)<NO[i,0]:
            x = np.insert(x, i, abs(maxX - NO[i,0]))
        else:
            x = np.insert(x, i, int(NO[i,0]))

    #코 배열을 가져와 y값을 y배열에 넣는다
    #값이 0 이면 0을 넣어주고 왼쪽 아래를 0으로 시작하기 위해 y값을 뒤집어 준다
    y = []
    for i in range(0, len(NO)):
        if NO[i,1] == 0:
            y = np.insert(y, i, 0)
            continue
        y = np.insert(y, i, abs(maxY - NO[i,1]))

    return x , y

def NeckKeypoint(NE, maxX, maxY):
    x2 = []
    for i in range(0, len(NE)):
        if NE[i,0] == 0:
            x2 = np.insert(x2, i, 0)
            continue
        elif (maxX/2)<NE[i,0]:
            x2 = np.insert(x2, i, abs(maxX - NE[i,0]))
        else:
            x2 = np.insert(x2, i, NE[i,0])

    y2 = []
    for i in range(0, len(NE)):
        if NE[i,1] == 0:
            y2 = np.insert(y2, i, 0)
            continue
        y2 = np.insert(y2, i, abs(maxY - NE[i,1]))

    return x2 , y2

NO1, NE1 = headkeypoints("1")
maxX, maxY = Framescale('/home/ms/frame/frame_10.jpg')
x, y = NoseKeypoint(NO1, maxX, maxY)
x2, y2 = NeckKeypoint(NE1, maxX, maxY)

NO2, NE2 = headkeypoints("2")
maxX2, maxY2 = Framescale('/home/ms/frame/frame_20.jpg')
x3, y3 = NoseKeypoint(NO2, maxX2, maxY2)
x4, y4 = NeckKeypoint(NE2, maxX2, maxY2)
'''
#코와 목의 각도 구하기
def getDegree(x1, y1, x2, y2):
    PI = 3.14
    Angle = []
    if len(x1)<len(x2):
    	leng = x2
    else:
    	leng = x1

    for i in range(len(leng)):
    	if y1[i] == 0 or y2[i] == 0 or x1[i] == 0 or x2[i] == 0:
    		Angle.append(0)
    		continue
    	Angle.append(math.atan2(abs(y1[i] - y2[i]), abs(x1[i] - x2[i])) * 180 / PI)

    return Angle 

'''
#머리 높이 비교하기 --- 미완성
def CompairHead():
    for hei in y:
        maxH = maxHC = count = 0
        if maxH<hei:
            maxH = hei
            count += 1
        elif maxH > hei:
            maxHC = count
            break

    for hei in y3:
        maxH2 = maxHC2 = count = 0
        if maxH2<wid:
            maxH2 = hei
            count += 1
        elif maxH2 > hei:
            maxHC2 = count
            break

    base_Video = getDegree(x, y, x2, y2)
    Compair_Video = getDegree(x3,y3,x4,y4)
    
    if len(base_Video) < len(Compair_Video):
        maxl = len(base_Video)
    else: maxl = len(Compair_Video)
    for i in range(0, maxl):
        value = base_Video[maxHC+i]
'''
#for i in range(0, if len(x)<len(x3): abs(len(x3))):
#    print(abs(Angle[i] - Angle2[i]))
'''
plt.subplot(121)
plt.plot(x, y, 'o', label = 'NO')
plt.plot(x2, y2, 'o', label = 'NE')
plt.subplot(122)
plt.plot(x3, y3, 'o', label = 'NO2')
plt.plot(x4, y4, 'o', label = 'NE2')


plt.xlabel('x')
plt.ylabel('y')

plt.title('compair')

plt.legend()

plt.show()
'''


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
    	'''
    	path = ('/home/ms/frame/frame_2'+ str(i) +'.jpg')

    	image = cv2.imread(path)
    	cv2.imshow("Moon", image)
    	cv2.waitKey(20)
    	'''
    	if i in tooH:
    		allarray.insert(count, "머리를 너무 높이 들었습니다. 머리를 내려주세요 ")
    		count += 1
    	elif i in tooL:
    		allarray.insert(count, "머리를 너무 내렸습니다. 머리를 올려주세요 ")
    		count += 1
    	else:
    		allarray.insert(count, "머리 높이가 정확합니다! ")
    		count += 1
    
    cv2.destroyAllWindows()
    return allarray
