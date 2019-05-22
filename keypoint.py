import numpy as np
import cv2
import math

#동영상 번호와 원하는 포인트 부분의 번호를 입력하면 
#입력한 포인트의 대한 x, y 값의 배열을 얻을 수 있다

def keypoint(num, point):
    if (point < 0) and (point > 14) :
        return "The range of points is wrong."

    Key = np.zeros((1,3))

    try:
    	image = cv2.imread("/home/ms/frame/frame_"+ str(num) +"0.jpg")        
    except FileNotFoundError:
        return "frame File not found"


    height, width, channel = image.shape
    #Nose , count = 0  
    count = 0
    Nose = 0
    #npy 파일을 불러오고 거기서 nose의 값만 가져와 새로운 배열을 만든다
    while True:
        
        try:
            arr = np.load("/home/ms/test/array_"+ str(num) +"%d.npy"% count)
            test += 1
        except FileNotFoundError:
            break

        #코의 값 중 유효값한 값을 가져옴

        if Nose == 0:
            Nose = int(arr[0, 0, 0])
        #---    
        if count == 0:
            for i in range(3):
                Key[0, i] = arr[0, point, i]   
               
        else:
            try:
                Key = np.insert(Key, count, arr[0, point], axis=0)        
            except IndexError:
                Key = np.insert(Key, count, 0, axis=0)        
        count += 1

    #코 배열을 가져와 x값을 x배열에 넣는다
    #값이 0 이면 0을 넣어주고 x값이 가로 크기/2 보다 크면 머리가 왼쪽으로 오게 바꿔준다
    x = []
    for i in range(0, len(Key)):
        if Key[i,0] == 0:
            x = np.insert(x, i, 0)
            continue
        elif (width/2)<Nose:
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

    return x , y

#print(keypoint("1", 0))