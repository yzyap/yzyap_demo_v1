from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.http import HttpResponse
from . import forms
from . import code_server_comm
from .code_server_comm import codeServerComm
import cv2
import numpy as np
import requests
import os
import time
from .video_source import VideoSource
from .dnn_object_detection import DnnObjectDetection
import json
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse

vs = VideoSource()

def generate_code_file(filename, template, code):
	if template is not None:
		complete_code = template + "\r\n" + code
	else:
		complete_code = code+"\r\n"
	file_handle = open(filename, "w")
	file_handle.write(complete_code)
	file_handle.flush()
	file_handle.close()

		
# Create your views here.
def home(request):
	template_data = {}
	csc = codeServerComm()
	if request.method == 'POST':
		form = forms.CodeExecutorForm(request.POST)
		template_data['form'] = form		
		if form.is_valid():
			if 'submit_code' in request.POST:			
				code = form.cleaned_data['code']
				path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
				print(path)
				filename = os.path.join(path, r"flask_runner\package\blockly_code.py")
				print(filename)
				generate_code_file(filename, None,code)
				
				csc.run_server_thread()
				return render(request, 'streamapp/home.html', template_data)

			elif 'terminate_code' in request.POST:
					print("code server terminating")
					response = requests.get('http://127.0.0.1:5000/shutdown')
					template_data['log'] = "Code Server Terminated"
					return render(request, 'streamapp/home.html', template_data)
			
		else:
			template_data['log'] = "Cannot sanitize form data"
			return render(request, 'streamapp/home.html', template_data)

	else:
		form = forms.CodeExecutorForm()
		template_data['form'] = form
		template_data['log'] = "New Code Project"
		return render(request, 'streamapp/home.html', template_data)

def gen(vs):

  objDetector = DnnObjectDetection(r"yolo_models/MobileNet_SSD_v3/coco.names",
    r"yolo_models/MobileNet_SSD_v3/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt",
      r"yolo_models/MobileNet_SSD_v3/frozen_inference_graph.pb")

  
  video = cv2.VideoCapture("http://192.168.1.43:8080/?action=stream")	
  #video = cv2.VideoCapture("http://192.168.1.35:8081/?action=stream")	


  #the first image is a bit darker so i get 30 frames to initialize camera
  #and get rid of this dark first frame.
    # We give some time for the camera to setup
  time.sleep(3)

  for i in range(10):
    success, image = video.read()
    
  #start the actual streaming
  while video.isOpened():		
    success, image = video.read()
    frame = objDetector.runModel(image)
    ret, jpeg = cv2.imencode('.jpg', frame)
    frame = jpeg.tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		

        		
def video_feed(request):
	return StreamingHttpResponse(gen(VideoSource()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def nesne_ogrenme(request):
	template_data = {}
	if request.method == 'POST':
		form = forms.NesneOgrenmeForm(request.POST)
		template_data['form'] = form
		if form.is_valid():
			if 'teach' in request.POST:
				bbox = (form.cleaned_data['form_x'],
							form.cleaned_data['form_y'],
								form.cleaned_data['form_width'],
									form.cleaned_data['form_height'])

				bb_etiket = form.cleaned_data['form_etiket']

				#tracker = cv2.TrackerMOSSE_create()
				#ok = tracker.init(frame, bbox)

				print(bbox[0],bbox[1],bbox[2],bbox[3])
				return render(request, r'streamapp/nesne_ogrenme.html', template_data)

		else:
			template_data['log'] = "Cannot sanitize form data"
			return render(request, r'streamapp/nesne_ogrenme.html', template_data)

	else:
		form = forms.NesneOgrenmeForm()
		template_data['form'] = form
		template_data['log'] = "New Code Project"
		return 	render(request, 'streamapp/nesne_ogrenme.html', template_data)	

def learnobject(request):
  if request.is_ajax() and request.POST:
    items = ['item1', 'item2', 'item3',]
    data = json.dumps(items)
    print("ajax post received")
    return HttpResponse(data, content_type='application/json')    										    
  else:
    raise Http404

class SignUpView(CreateView):
  template_name = 'streamapp/signup.html'
  form_class = UserCreationForm  

  from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
  print("validate user name")
  username = request.GET.get('username', None)
  data = {
    'is_taken': User.objects.filter(username__iexact=username).exists()
  }
  if data['is_taken']:
    data['error_message'] = 'A user with this username already exists.'
  else:
    data['error_message'] = 'No error'
  
  return JsonResponse(data)


def index(request):
  if request.method == 'POST':
    form = forms.CodeExecutorForm(request.POST)
    if form.is_valid():
      pass
  else:
    form = forms.CodeExecutorForm()

  return render(request, 'streamapp/index.html', {'form': form})







										
