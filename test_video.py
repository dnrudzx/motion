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
        #sys.path.append('/[path]/openpose/build/python');
        sys.path.append('/home/ms/openpose/build/python');
        from openpose import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
#params[""] = ""
params["logging_level"] = 3
params["net_resolution"] = "656x368"
params["model_pose"] = "BODY_25"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
params["number_people_max"] = 1
#params["disable_blending"] = False
        # Ensure you point to the correct path where models are located
#params["model_folder"] = "/[path]/openpose/models/"
params["model_folder"] = "/home/ms/openpose/models/"

# Construct it from system arguments
# op.init_argv(args[1])
# oppython = op.OpenposePython()

# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

#video 
#video_dir("/[path]/video.avi")
#cap = cv2.VideoCapture("/home/ms/openpose/examples/media/push3.avi")
#cap = cv2.VideoCapture(sys.argv[1])
cap = cv2.VideoCapture("/home/ms/push5R.avi")

#save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('push5RT.avi', fourcc, 25.0, (int(cap.get(3)),int(cap.get(4))))

count = 0
# Process Image
datum = op.Datum()
while(cap.isOpened()):
    ret, frame = cap.read()
    datum = op.Datum()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop([datum])

    print("Body keypoints: \n" + str(datum.poseKeypoints))
  
    print(datum.poseKeypoints.shape)

    np.save("./test/array_3%d" % count, datum.poseKeypoints)
    cv2.imwrite("./frame/frame_3%d.jpg"%count, datum.cvOutputData)
    count += 1

    out.write(datum.cvOutputData)
    
    cv2.imshow("push up", datum.cvOutputData)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

def keypoint():
	return datum.poseKeypoints
