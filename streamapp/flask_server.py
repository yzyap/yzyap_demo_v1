#!/usr/bin/env python
from flask import Flask, render_template, Response
from flask import request

from .camera import Camera
from importlib import reload
from .blockly_code import blockly_code

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def generate_code_file(template, code):
    filename = "blockly_code.py"
    if template is not None:
        complete_code = template + "\r\n" + code
    else:
        complete_code = code+"\r\n"
    file_handle = open(filename, "w")
    file_handle.write(complete_code)
    file_handle.flush()
    file_handle.close()    

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/loadcodefile')
def loadcodefile():
    data = request.get_data()
    print("code file", data)
    #generate_code_file(None, data)
    return 'Code file generated...'    

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

def RunFlaskServer():
    app.run(host='0.0.0.0', debug=True)