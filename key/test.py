import numpy as np
import matplotlib.pyplot as plt

def pprint(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

LS =np.empty((1,3))
LE =np.zeros((1,3))
LW =np.zeros((1,3))
LS2 =np.empty((1,3))
LE2 =np.zeros((1,3))
LW2 =np.zeros((1,3))
count = 0

while True:
    try:
        a = np.load("./array_1%d.npy" % count)
    except FileNotFoundError:
        break

    if count == 0:
        LS[0, 0] = a[0, 5, 0]
        LS[0, 1] = a[0, 5, 1]
        LS[0, 2] = a[0, 5, 2]
        LE[0, 0] = a[0, 6, 0]
        LE[0, 1] = a[0, 6, 1]
        LE[0, 2] = a[0, 6, 2]
        LW[0, 0] = a[0, 7, 0]
        LW[0, 1] = a[0, 7, 1]
        LW[0, 2] = a[0, 7, 2]

        pprint(LS)
        pprint(LE)
        pprint(LW)
    else:
        LS = np.insert(LS, count, a[0, 5], axis=0)
        LE = np.insert(LE, count, a[0, 6], axis=0)
        LW = np.insert(LW, count, a[0, 7], axis=0)
    count += 1

#push3_1R.avi
count = 0
while True:
    try:
        a = np.load("./array_2%d.npy" % count)
    except FileNotFoundError:
        break

    if count == 0:
        LS2[0, 0] = a[0, 5, 0]
        LS2[0, 1] = a[0, 5, 1]
        LS2[0, 2] = a[0, 5, 2]
        LE2[0, 0] = a[0, 6, 0]
        LE2[0, 1] = a[0, 6, 1]
        LE2[0, 2] = a[0, 6, 2]
        LW2[0, 0] = a[0, 7, 0]
        LW2[0, 1] = a[0, 7, 1]
        LW2[0, 2] = a[0, 7, 2]

        pprint(LS2)
        pprint(LE2)
        pprint(LW2)
    else:
        LS2 = np.insert(LS2, count, a[0, 5], axis=0)
        LE2 = np.insert(LE2, count, a[0, 6], axis=0)
        LW2 = np.insert(LW2, count, a[0, 7], axis=0)
    count += 1

#push3R.avi
x = []
for i in range(0, len(LS)):
    if LS[i,0] == 0:
        x = np.insert(x, i, 0)
        continue
    x = np.insert(x, i, LS[i,0])
y = []
for i in range(0, len(LS)):
    if LS[i,1] == 0:
        y = np.insert(y, i, 0)
        continue
    y = np.insert(y, i, LS[i,1])

x2 = []
for i in range(0, len(LE)):
    if LE[i,0] == 0:
        x2 = np.insert(x2, i, 0)
        continue
    x2 = np.insert(x2, i, LE[i,0])
y2 = []
for i in range(0, len(LE)):
    if LE[i,1] == 0:
        y2 = np.insert(y2, i, 0)
        continue
    y2 = np.insert(y2, i, LE[i,1])
x3 = []
for i in range(0, len(LW)):
    if LW[i,0] == 0:
        x3 = np.insert(x3, i, 0)
        continue
    x3 = np.insert(x3, i, LW[i,0])
y3 = []
for i in range(0, len(LW)):
    if LW[i,1] == 0:
        y3 = np.insert(y3, i, 0)
        continue
    y3 = np.insert(y3, i, LW[i,1])

#push3_1R.avi
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



plt.plot(x, y, 'o', label = 'LS')

plt.plot(x_1, y_1, 'o', label = 'LS2')

plt.xlabel('x')
plt.ylabel('y')

plt.title('compair')

plt.legend()

plt.show()
