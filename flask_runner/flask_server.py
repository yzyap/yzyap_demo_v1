#!/usr/bin/env python
import cv2
import time
import os.path
import sys
from flask import Flask, render_template, Response
from flask import request

from package.camera import Camera
from importlib import reload
import package.blockly_code 
from package.yolo_obj_detect import yolo_detect

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/islive')
def islive():
    return "live"

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):    
    blockly_module = reload(package.blockly_code)
    return blockly_module.blockly_code(camera)

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True) 
    