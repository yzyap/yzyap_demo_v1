#!/usr/bin/env python
from flask import Flask, render_template, Response
from flask import request

from camera import Camera
from importlib import reload
import blockly_code

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

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):    
    blockly_module = reload(blockly_code)
    return blockly_module.blockly_code(camera)


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)