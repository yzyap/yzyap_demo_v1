import cv2,os,urllib.request
import numpy as np

class Camera:

    stream_source = None
    video = None    

    def init(self):
        self.stream_source = "http://192.168.1.43:8080/?action=stream"
        #self.video = cv2.VideoCapture(self.stream_source)
        self.video = cv2.VideoCapture(0)
        return self.video

    def get_frame(self):
        success, image = self.video.read()
        image = cv2.Canny(image,100,200)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()