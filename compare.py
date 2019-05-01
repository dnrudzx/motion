import sys
import cv2
import os
from sys import platform
import argparse
import video_pose

dir_path = os.path.dirname(os.path.realpath(__file__))
try:
        #sys.path.append('/[path]/openpose/build/python');
        sys.path.append('/home/ms/openpose/build/python');
        from openpose import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

#video
point = video_pose.keypoint()

print(str(point))
