import numpy as np
import cv2
import math

def path(name):
    if str(name) == "bpush":
        frame_path = "/home/ms/frame/frame_1"
        array_path = "/home/ms/test/array_1"
    elif str(name) == "ppush":
        frame_path = "/home/ms/frame/frame_2"
        array_path = "/home/ms/test/array_2"
    elif str(name) == "blunge":
        frame_path = "/home/ms/frame/lunge_frame/Bframe_"
        array_path = "/home/ms/test/lunge_array/Barray_"
    elif str(name) == "plunge":
        frame_path = "/home/ms/frame/lunge_frame/Pframe_"
        array_path = "/home/ms/test/lunge_array/Parray_"
    elif str(name) == "bclimber":
        frame_path = "/home/ms/frame/climber_frame/Bframe_"
        array_path = "/home/ms/test/climber_array/Barray_"
    elif str(name) == "pclimber":
        frame_path = "/home/ms/frame/climber_frame/Pframe_"
        array_path = "/home/ms/test/climber_array/Parray_"

    return frame_path, array_path

#동영상 번호와 원하는 포인트 부분의 번호를 입력하면 
#입력한 포인트의 대한 x, y 값의 배열을 얻을 수 있다
# 0: 코, 1: 목 2:오른쪽 어꺠 3: 오른쪽 팔꿈치 4:오른쪽 손목 5: 왼쪽 어꺠 6: 왼쪽 팔꿈치 
# 7: 왼쪽 손목 8: 중앙 엉덩이 9: 오른쪽 엉덩이  10:오른쪽 무릅 11: 오른쪽 발목 
# 12: 왼쪽 엉덩이 13: 왼쪽 무릅 14: 왼쪽 발목
def keypoint(name, point):
    frame_path, array_path = path(name)

    if (point < 0) and (point > 25) :
        return "The range of points is wrong."

    Key = np.zeros((1,3))

    try:
    	image = cv2.imread(frame_path +"0.jpg")        
    except FileNotFoundError:
        return "frame File not found"


    height, width, channel = image.shape

    count = 0
    Nose = 0
    Neck = 0
    #npy 파일을 불러오고 거기서 원하는 point 값만 가져와 새로운 배열을 만든다
    while True:
        
        try:
            arr = np.load(array_path +"%d.npy"% count)
        except FileNotFoundError:
            break

        #방향을 같게 하기 위해 코와 목의 값 중 유효한 동영상의 x값을 가져옴
        if Nose == 0 and int(arr[0, 0, 0]) !=0 and Neck == 0 and int(arr[0, 1, 0]) !=0:
            Nose = int(arr[0, 0, 0])
            Neck = int(arr[0, 1, 0])
        #
        if count == 0:
            for i in range(3):
                Key[0, i] = arr[0, point, i]
               
        else:
            try:
                Key = np.insert(Key, count, arr[0, point], axis=0)        
            except IndexError:
                Key = np.insert(Key, count, 0, axis=0)        
        count += 1
    #원하는 point 값을 가져와 x축만의 배열을 만들어 준다.
    #코와 목 값을 가져와 방향을 정한다.
    x = []
    for i in range(0, len(Key)):
        if Key[i,0] == 0:
            x = np.insert(x, i, 0)
            continue
        else:
            if Neck<Nose:
                x = np.insert(x, i, abs(width - Key[i,0]))
            else:
                x = np.insert(x, i, int(Key[i,0]))

        #코 배열을 가져와 y값을 y배열에 넣는다
        #동영상 포인트값을 가져올때 상하 반전되어 가져오기 때문에 최대 y 값에서 y값을 뺴준다.
    y = []
    for i in range(0, len(Key)):
        if Key[i,1] == 0:
            y = np.insert(y, i, 0)
            continue
        y = np.insert(y, i, abs(height - Key[i,1]))

    Rx = []
    Ry = []

    xavg = keyavg(x)
    yavg = keyavg(y)

    for i in range(len(x)):
    	if x[i] == 0:
    		Rx.append(x[i])
    		continue
    	elif i == 0:
    		Rx.append(x[i])
    		continue
    	elif i == (len(x)-1):
    		Rx.append(x[i])
    		break
    	elif x[i+1] != 0 and (xavg * 2.0) < (abs(x[i+1]-x[i])):
    		Rx.append(0)
    	else:
    		Rx.append(x[i])

    for i in range(len(y)):
    	if y[i] == 0:
    		Ry.append(y[i])
    		continue
    	elif i == 0:
    		Ry.append(y[i])
    		continue
    	elif i == (len(y)-1):
    		Ry.append(y[i])
    		break
    	elif y[i+1] != 0 and (yavg * 2.0) < (abs(y[i+1]-y[i])):
    		Ry.append(0)
    	else:
    		Ry.append(y[i])

    return Rx , Ry
#point값이 튀였는지 여부를 확인하기 위해서 평균 변화량을 구함
def keyavg(x):
	Rx = []
	result = 0

	for i in range(len(x)):
		if x[i] == 0:
			continue
		elif i == len(x)-1:
			break
		elif x[i+1] != 0:
			Rx.append(abs(x[i+1] - x[i]))
	for i in Rx:
		result += i
		
	return result/(len(Rx))
#print(keypoint("1", 0))

# 두점 사이의 거리 구하기
def height(name):
	frame_path, array_path = path(name)
	
	count = 0
	array = [0, 1, 8, 9, 10, 11, 12, 13, 14]
	con = 0

	NO_x,NE_x,MH_x,RH_x,RK_x,RA_x,LH_x,LK_x,LA_x = 0,0,0,0,0,0,0,0,0
	NO_y,NE_y,MH_y,RH_y,RK_y,RA_y,LH_y,LK_y,LA_y = 0,0,0,0,0,0,0,0,0
	while con==0:
		try:
			arr = np.load(array_path +"%d.npy"% count)
		except FileNotFoundError:
			break

		count1 = 0
		for num in array:
			if int(arr[0, num, 0]) == 0 or int(arr[0, num, 1]) == 0:
				continue
			else:
				count1 +=1

		if count1 == 9:
			NO_x, NO_y = int(arr[0, 0, 0]), int(arr[0, 0, 1])
			NE_x, NE_y = int(arr[0, 1, 0]), int(arr[0, 1, 1])
			MH_x, MH_y = int(arr[0, 8, 0]), int(arr[0, 8, 1])
			RH_x, RH_y = int(arr[0, 9, 0]), int(arr[0, 9, 1])
			RK_x, RK_y = int(arr[0, 10, 0]), int(arr[0, 10, 1])
			RA_x, RA_y = int(arr[0, 11, 0]), int(arr[0, 11, 1])
			LH_x, LH_y = int(arr[0, 12, 0]), int(arr[0, 12, 1])
			LK_x, LK_y = int(arr[0, 13, 0]), int(arr[0, 13, 1])
			LA_x, LA_y = int(arr[0, 14, 0]), int(arr[0, 14, 1])
			con = 1

	d1 = distance(NO_x, NO_y, NE_x, NE_y)
	d2 = distance(NE_x, NE_y, MH_x, MH_y)
	drh = distance(RH_x, RH_y, RK_x, RK_y)
	drk = distance(RK_x, RK_y, RA_x, RA_y)
	dlh = distance(LH_x, LH_y, LK_x, LK_y)
	dlk = distance(LK_x, LK_y, LA_x, LA_y)

	r = d1 + d2 + drh + drk
	l = d1 + d2 + dlh + dlk

	avg1 = (r+l)/2

	return 170/avg1



def distance(x1, y1, x2, y2):
	x = abs(x2 - x1)
	y = abs(y2 - y1)

	d = math.sqrt((x * x) + (y * y))

	return d
