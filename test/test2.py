import numpy as np
import matplotlib.pyplot as plt

def pprint(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

count = 0

a = np.load("./array_11.npy")

x_1 = []
for i in range(0, len(a[0])):
    if a[0,i,0] == 0:
        x_1 = np.insert(x_1, i, 0)
        continue
    x_1 = np.insert(x_1, i, a[0,i,0])
y_1 = []
for i in range(0, len(a[0])):
    if a[0,i,1] == 0:
        y_1 = np.insert(y_1, i, 0)
        continue
    y_1 = np.insert(y_1, i, a[0,i,1])

print(x_1)
print(y_1)

#push3_1R.avi

#plt.plot(x, y, 'o', label = 'LS')

plt.plot(x_1, y_1, 'o', label = 'LS2')

plt.xlabel('x')
plt.ylabel('y')

plt.title('compair')

plt.legend()

plt.show()


