import numpy as np
import cv2
import math

def keypoints(num):
    NO = np.zeros((1,3))
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


    count = 0

    while True:
        try:
            arr = np.load("../test/array_"+ num +"%d.npy"% count)
        except FileNotFoundError:
            break
    
        if count == 0:
            for i in range(3):
                NO[0, i] = arr[0, 0, i]   
                NE[0, i] = arr[0, 1, i]
                RS[0, i] = arr[0, 2, i]
                RE[0, i] = arr[0, 3, i]
                RW[0, i] = arr[0, 4, i]
                LS[0, i] = arr[0, 5, i]
                LE[0, i] = arr[0, 6, i]
                LW[0, i] = arr[0, 7, i]
                MI[0, i] = arr[0, 8, i]
                RH[0, i] = arr[0, 9, i]
                RK[0, i] = arr[0, 10, i]
                RA[0, i] = arr[0, 11, i]
                LH[0, i] = arr[0, 12, i]
                LK[0, i] = arr[0, 13, i]
                LA[0, i] = arr[0, 14, i]

        else:
            try:
                NO = np.insert(NO, count, a[0, 0], axis=0)        
                NE = np.insert(NE, count, a[0, 1], axis=0)
                RS = np.insert(RS, count, a[0, 2], axis=0)
                RE = np.insert(RE, count, a[0, 3], axis=0)
                RW = np.insert(RW, count, a[0, 4], axis=0)
                LS = np.insert(LS, count, a[0, 5], axis=0)
                LE = np.insert(LE, count, a[0, 6], axis=0)
                LW = np.insert(LW, count, a[0, 7], axis=0)
                MI = np.insert(MI, count, a[0, 8], axis=0)
                RH = np.insert(RH, count, a[0, 9], axis=0)
                RK = np.insert(RK, count, a[0, 10], axis=0)
                RA = np.insert(RA, count, a[0, 11], axis=0)
                LH = np.insert(LH, count, a[0, 12], axis=0)
                LK = np.insert(LK, count, a[0, 13], axis=0)
                LA = np.insert(LA, count, a[0, 14], axis=0)

            except IndexError:
                NO = np.insert(NO, count, 0, axis=0)        
                NE = np.insert(NE, count, 0, axis=0)
                RS = np.insert(RS, count, 0, axis=0)
                RE = np.insert(RE, count, 0, axis=0)
                RW = np.insert(RW, count, 0, axis=0)
                LS = np.insert(LS, count, 0, axis=0)
                LE = np.insert(LE, count, 0, axis=0)
                LW = np.insert(LW, count, 0, axis=0)
                MI = np.insert(MI, count, 0, axis=0)
                RH = np.insert(RH, count, 0, axis=0)
                RK = np.insert(RK, count, 0, axis=0)
                RA = np.insert(RA, count, 0, axis=0)
                LH = np.insert(LH, count, 0, axis=0)
                LK = np.insert(LK, count, 0, axis=0)
                LA = np.insert(LA, count, 0, axis=0)
        count += 1

    return NO, NE
