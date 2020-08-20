from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.http import HttpResponse
from streamapp.camera import VideoCamera, IPWebCam
from . import forms
from . import CompilerUtils
from .CompilerUtils import Compiler
import cv2
import numpy as np

executor = Compiler()
video = cv2.VideoCapture("http://192.168.1.43:8080/?action=stream")

# Create your views here.
def index(request):
	template_data = {}
	if request.method == 'POST':
		if 'submit_code' in request.POST:
			form = forms.CodeExecutorForm(request.POST)
			if form.is_valid():
				code = form.cleaned_data['code']
				executor.set_code(code)
				execution_result = executor.execute()
				executor.delete_code_file()
				return HttpResponse("Worked!")
			else:
				return HttpResponse("Cannot sanitize form data")

		elif 'terminate_code' in request.POST:
			if not executor:
				executor.terminate()
				return HttpResponse("Terminated!")
			else:
				return HttpResponse("No valid run session!")
	else:
		form = forms.CodeExecutorForm()
		template_data['form'] = form
		return render(request, 'streamapp/home.html', template_data)


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen1(camera):	
	while True:
		success, image = video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		edges = cv2.Canny(image,100,200)
		ret, jpeg = cv2.imencode('.jpg', edges)

		frame = jpeg.tobytes()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')				

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed_processed(request):
	return StreamingHttpResponse(gen1(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')
