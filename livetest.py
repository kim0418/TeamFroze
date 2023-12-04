from flask import Flask, Response
import os
import subprocess

app = Flask(__name__)

def generate_video():
    cmd = ['libcamera-vid', '-t', '0', '-o', '-']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        data = p.stdout.read(512)
        if len(data) == 0:
            break
        yield data

@app.route('/')
def index():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
