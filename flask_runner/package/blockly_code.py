import cv2
from .camera import Camera
import time

def blockly_code(camera):
    video = cv2.VideoCapture(r'C:\test.mp4')
    while True:
        time.sleep(0.05)
        success, image = video.read()
        image = cv2.Canny(image,100,200)
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
