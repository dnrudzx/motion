import numpy as np
import cv2
import math


#코의 대한 x, y 값의 배열을 얻을 수 있다
def NOSE(num):
    NO = np.zeros((1,3))

    count = 0
    #npy 파일을 불러오고 거기서 nose의 값만 가져와 새로운 배열을 만든다
    while True:
        try:
            arr = np.load("/home/ms/test/array_"+ num +"%d.npy"% count)
        except FileNotFoundError:
            break
    
        if count == 0:
            for i in range(3):
                NO[0, i] = arr[0, 0, i]   
               
        else:
            try:
                NO = np.insert(NO, count, arr[0, 0], axis=0)        
            except IndexError:
                NO = np.insert(NO, count, 0, axis=0)        
        count += 1
    #코 배열을 가져와 x값을 x배열에 넣는다
    #값이 0 이면 0을 넣어주고 x값이 가로 크기/2 보다 크면 머리가 왼쪽으로 오게 바꿔준다
    x = []
    for i in range(0, len(NO)):
        if NO[i,0] == 0:
            x = np.insert(x, i, 0)
            continue
        else:
            x = np.insert(x, i, int(NO[i,0]))

        #코 배열을 가져와 y값을 y배열에 넣는다
    y = []
    for i in range(0, len(NO)):
        if NO[i,1] == 0:
            y = np.insert(y, i, 0)
            continue
        y = np.insert(y, i, abs(NO[i,1]))

    return x , y


'''
    NE = np.zeros((1,3))
    RS = np.zeros((1,3))
    RE = np.zeros((1,3))
    RW = np.zeros((1,3))
    LS = np.zeros((1,3))
    LE = np.zeros((1,3))
    LW = np.zeros((1,3))
    MI = np.zeros((1,3))
    RH = np.zeros((1,3))
    RK = np.zeros((1,3))
    RA = np.zeros((1,3))
    LH = np.zeros((1,3))
    LK = np.zeros((1,3))
    LA = np.zeros((1,3))
'''