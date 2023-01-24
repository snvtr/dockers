from app import app
from flask import Response
import urllib.request
import os

HOST = os.environ.get('DB_HOST') or 'localhost'

@app.route('/')
def index():
    contents = bytes.decode(urllib.request.urlopen('http://'+HOST+':7000').read())
    items = contents.split(',')
    print(items)
    answer = '{ "id": "%s",\n"adjective": "%s",\n"noun": "%s" }' % (items[0], items[1], items[2])
    return Response(answer, mimetype='text/json')