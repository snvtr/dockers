from app import app
from flask import render_template
import os
import socket

@app.route("/")
def index():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = 'unknown'
    finally:
        s.close()
    return render_template('index.html', ip=ip)
