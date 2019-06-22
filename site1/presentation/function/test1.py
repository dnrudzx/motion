#동영상을 트래킹해서 배열/프래임 저장
# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
import numpy as np

# Import Openpose (Windows/Ubuntu/OSX)
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # sys.path.append('/[path]/openpose/build/python');
    #함수 임폴트
    sys.path.append('/home/ms/openpose/build/python');
    from openpose import pyopenpose as op
except ImportError as e:
    print(
        'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
# params[""] = ""
#동영상 트래킹할떄 추가로 설정
params["logging_level"] = 3
params["net_resolution"] = "656x368"
params["model_pose"] = "BODY_25"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
params["number_people_max"] = 1
# params["disable_blending"] = False
# Ensure you point to the correct path where models are located
# params["model_folder"] = "/[path]/openpose/models/"
params["model_folder"] = "/home/park/openpose/models/"

# Construct it from system arguments
# op.init_argv(args[1])
# oppython = op.OpenposePython()

# Starting OpenPose
#opWrapper을 실행해서 트래킹을 시작



def traking(video_name):
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    cap = cv2.VideoCapture("/home/ms/openpose/build/examples/tutorial_api_python/site1/media/%s"%str(video_name))
    #cap = cv2.VideoCapture("/home/park/openpose/build/examples/tutorial_api_python/firstdjango/site1/media/The_Power_of_Teamwork_-_Funny_Animation.mp4")
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('media/output/traking.avi', fourcc, 25.0, (int(cap.get(3)), int(cap.get(4))))

    count = 0
    datum = op.Datum()
    #print("/home/park/openpose/build/example/tutorial_api_python/firstdjango/site1/media/"+str(video_name))
    print(cap.isOpened())
    while (cap.isOpened()):
        if((cap.get(cv2.CAP_PROP_POS_FRAMES))==(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            break
        ret, frame = cap.read()
        datum = op.Datum()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])
        np.save("media/output/array/array_3%d" % count, datum.poseKeypoints)
        cv2.imwrite("media/output/frame/frame_3%d.jpg" % count, datum.cvOutputData)
        count += 1
        out.write(datum.cvOutputData)
    cap.release()
    out.release()


