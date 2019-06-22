from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import math
from .function import renew, test1, keypoint_main


context_all = {}
# Create your views here.
def index(request):
    return render(request, 'presentation/index.html')

@csrf_exempt
def page2_1(request):
    return render(request, 'presentation/2_1.html')

@csrf_exempt
def page2_2(request):
    if request.method == 'POST':
        selected_pose = request.POST['pose']
        if selected_pose == '':
        	return render(request, 'presentation/2_1.html')
        context_all['selected_pose'] = selected_pose
        print(selected_pose)
        return render(request, 'presentation/2_2.html', context_all)

@csrf_exempt
def page2_3or4(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        context_all['mode'] = request.POST['mode']
        if context_all['mode'] == '1':
            context_all['video'] = fs.url("output/based_video/P_push.avi")
            return render(request, 'presentation/2_4.html', context_all)
        #if context_all['mode'] == '2':
        #    context_all['video'] = fs.url("traking.avi")
        #    return render(request, 'presentation/2_4.html', context_all)
        if context_all['mode'] == '3':
            return render(request, 'presentation/2_3.html', context_all)
        #if context_all['mode'] == '4':
        #    return render(request, 'presentation/2_3.html', context_all)

@csrf_exempt
def page2_4(request):
    fs = FileSystemStorage()
    if context_all['mode'] == '3':
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            name = fs.save(uploaded_file.name, uploaded_file)
            renew.renew()
            test1.traking(uploaded_file.name)
            context_all['speech'], context_all['speech_body'], context_all['speech_arm'] = keypoint_main.speech()
            context_all['video'] = fs.url(name)
            return render(request, 'presentation/2_4.html', context_all)
    #if context_all['mode'] == '4':
    #    if request.method == 'POST':
    #        uploaded_file = request.FILES['document']
    #        test1.traking(uploaded_file.name)
    #        context_all['video'] = fs.url("output/traking.avi")
    #        return render(request, 'presentation/2_4.html', context_all)
