import numpy as np
import matplotlib.pyplot as plt
import cv2

maxX = 0
maxY = 0

def pprint(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

def Videoscale(filename):
    cap = cv2.VideoCapture(filename)
    
    maxX = int(cap.get(3))
    maxY = int(cap.get(4))


def headkeypoints():
    NO =np.zeros((1,3))
    NE =np.zeros((1,3))

    count = 0

    while True:
        try:
            a = np.load("./array_1%d.npy" % count)
        except FileNotFoundError:
            break
    
        if count == 0:
            NO[0, 0] = a[0, 5, 0]
            NO[0, 1] = a[0, 5, 1]
            NO[0, 2] = a[0, 5, 2]
            NE[0, 0] = a[0, 6, 0]
            NE[0, 1] = a[0, 6, 1]
            NE[0, 2] = a[0, 6, 2]
    
            pprint(NO)
            pprint(NE)
        else:
            NO = np.insert(NO, count, a[0, 0], axis=0)
            NE = np.insert(NE, count, a[0, 1], axis=0)
        count += 1
        pprint(NO)
        pprint(NE)

    return NO, NE

#push3R.avi

NO, NE = headkeypoints()
Videoscale('/home/ms/frame/frame_10.jpg')

x = []
for i in range(0, len(NO)):
    if NO[i,0] == 0:
        x = np.insert(x, i, 0)
        continue
    x = np.insert(x, i, NO[i,0])

y = []
for i in range(0, len(NO)):
    if NO[i,1] == 0:
        y = np.insert(y, i, 0)
        continue
    y = np.insert(y, i, abs(maxY-NO[i,1]))
'''
x2 = []
for i in range(0, len(NE)):
    if NE[i,0] == 0:
        x2 = np.insert(x2, i, 0)
        continue
    x2 = np.insert(x2, i, NE[i,0])

y2 = []
for i in range(0, len(NE)):
    if NE[i,1] == 0:
        y2 = np.insert(y2, i, 0)
        continue
    y2 = np.insert(y2, i, NE[i,1])
'''
x2 = []
for i in range(0, len(NE)):
    if NE[i,0] == 0:
        x2 = np.insert(x2, i, 0)
        continue
    elif (i%10) != 0:
        x2 = np.insert(x2, i, 0)
        continue
    x2 = np.insert(x2, i, NE[i,0])

y2 = []
for i in range(0, len(NE)):
    if NE[i,1] == 0:
        y2 = np.insert(y2, i, 0)
        continue
    elif (i%10) != 0:
        y2 = np.insert(y2, i, 0)
        continue
    y2 = np.insert(y2, i, NE[i,1])
#push3_1R.avi
'''
x_1 = []
for i in range(0, len(LS2)):
    if LS2[i,0] == 0:
        x_1 = np.insert(x_1, i, 0)
        continue
    x_1 = np.insert(x_1, i, LS2[i,0])

y_1 = []
for i in range(0, len(LS2)):
    if LS2[i,1] == 0:
        y_1 = np.insert(y_1, i, 0)
        continue
    y_1 = np.insert(y_1, i, LS2[i,1])
'''


plt.plot(x, y, 'o', label = 'NO')

plt.plot(x2, y2, 'o', label = 'NE')

plt.xlabel('x')
plt.ylabel('y')

plt.title('compair')

plt.legend()

plt.show()
