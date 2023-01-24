from app import app
import urllib.request
import json
import os

BACK_HOST = os.environ.get('BACK_HOST') or 'localhost'

@app.route('/')
def index():
    contents = bytes.decode(urllib.request.urlopen('http://'+BACK_HOST+':5001').read())
    json_val = json.loads(contents)
    return '<html> got response from the whole chain:'+str(json_val)+'</html>'