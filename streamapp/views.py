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

def gen():
	#video = cv2.VideoCapture("http://192.168.1.43:8080/?action=stream")
	#video = cv2.imread('lena.jpg')
	video = cv2.VideoCapture(r'C:\test.mp4')
	while True:		
		success, image = video.read()
		ret, jpeg = cv2.imencode('.jpg', image)
		frame=jpeg.tobytes()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')		
	
def video_feed(request):
	return StreamingHttpResponse(gen(),
					content_type='multipart/x-mixed-replace; boundary=frame')						
