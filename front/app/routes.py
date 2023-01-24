from app import app
import urllib.request
import json
import os
from datetime import datetime
import requests

BACK_HOST = os.environ.get('BACK_HOST') or 'localhost'
LOGR_HOST = os.environ.get('LOGR_HOST') or 'localhost'

@app.route('/')
def index():
    logr('FRONT', 'INFO', 'query sent')
    contents = bytes.decode(urllib.request.urlopen('http://'+BACK_HOST+':5001').read())
    json_val = json.loads(contents)
    logr('FRONT', 'INFO', 'got response: '+str(json_val))
    return '<html> got response from the whole chain:'+str(json_val)+'</html>'

def logr(host, level, msg):
        req_str = (''.join(['http://',LOGR_HOST,':5002',
                   '/add?moment=',str(datetime.now()),
                   '&host=',host,
                   '&level=',level,
                   '&msg=',msg
                  ]))
        req = requests.get(req_str)
