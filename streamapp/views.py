from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.http import HttpResponse
from . import forms
from . import code_server_comm
from .code_server_comm import codeServerComm
import cv2
import numpy as np
import requests

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
				csc.run_server_thread()

#				if runserver_result == ExecutionStatus.ACC:
#					print("execute_acc")
#					response = requests.post("http://0.0.0.0:5000/loadcodefile", json={'code':code})
#					template_data['log'] = "Code Server Worked"
#				else:
#					print("Code Server Proble")
#					template_data['log'] = "Code Server Problem!"
#
				return render(request, 'streamapp/home.html', template_data)

			elif 'terminate_code' in request.POST:
					response = requests.get('http://0.0.0.0:5000/shutdown')
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
	video = cv2.VideoCapture("http://192.168.1.43:8080/?action=stream")
	while True:		
		success, image = video.read()
		ret, jpeg = cv2.imencode('.jpg', image)
		frame=jpeg.tobytes()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')		
	
def video_feed(request):
	return StreamingHttpResponse(gen(),
					content_type='multipart/x-mixed-replace; boundary=frame')						
