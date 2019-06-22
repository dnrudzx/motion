import shutil
import os
def renew():
	try:
		shutil.rmtree('/home/ms/openpose/build/examples/tutorial_api_python/site1/media/output/frame')
		shutil.rmtree('/home/ms/openpose/build/examples/tutorial_api_python/site1/media/output/array')
		os.mkdir('/home/ms/openpose/build/examples/tutorial_api_python/site1/media/output/array')
		os.mkdir('/home/ms/openpose/build/examples/tutorial_api_python/site1/media/output/frame')
	except OSError as e:
		if e.errno == 2:
			print('No such file or directory to remove')
			pass
		else:
			raise