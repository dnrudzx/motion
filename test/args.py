import sys
import os

def hi(arrays):
    for array in arrays:
        print("%s\n" % array)


array = ["array1", "array2", "array3"]

path_dir = '/home/ms/test'

file_list = os.listdir(path_dir)
file_list_py = [file for file in file_list if file.endswith("_1*.npy")]

file_list_py.sort()

print(file_list)
print ("file_list_py: {}".format(file_list_py))
    
