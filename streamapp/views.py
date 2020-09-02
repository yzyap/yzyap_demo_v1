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
def index(request):
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
	video = cv2.VideoCapture(0)	
	while video.isOpened():		
		success, image = video.read()
		ret, jpeg = cv2.imencode('.jpg', image)			
		frame = jpeg.tobytes()
		if frame != None:
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




										
