from app import app
from flask import Response
import urllib.request
import os
import requests
from datetime import datetime
import socket

DB_HOST = os.environ.get('DB_HOST') or 'localhost'
LOGR_HOST = os.environ.get('LOGR_HOST') or 'localhost'

@app.route('/')
def index():
    logr('BACK', 'INFO', 'query sent')
    contents = bytes.decode(urllib.request.urlopen('http://'+DB_HOST+':7000').read())
    logr('BACK', 'INFO', 'got response: %s' % contents)
    items = contents.split(',')
    print(items)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        my_ip = s.getsockname()[0]
    except:
        my_ip = 'unknown'
    finally:
        s.close()
    answer = '{\n"id": "%s",\n"adjective": "%s",\n"noun": "%s",\n"my_ip": "%s"\n}' % (items[0], items[1], items[2], my_ip)
    logr('BACK', 'INFO', 'got response: '+answer.replace('\n', ' '))
    return Response(answer, mimetype='text/json')

def logr(host, level, msg):
        req_str = (''.join(['http://',LOGR_HOST,':5002',
                   '/add?moment=',str(datetime.now()),
                   '&host=',host,
                   '&level=',level,
                   '&msg=',msg
                  ]))
        req = requests.get(req_str)