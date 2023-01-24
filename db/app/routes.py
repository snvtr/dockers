from flask import Response
from app import app, db
from app.models import Greetings
from random import randrange
import requests
import os
from datetime import datetime

LOGR_HOST = os.environ.get('LOGR_HOST') or 'localhost'

@app.route('/')
def index():
    x = Greetings.query.get(randrange(1,10))
    logr('DB', 'INFO', 'got response: '+','.join([str(x.id), x.adj, x.noun]))    
    return Response(','.join([str(x.id), x.adj, x.noun]), mimetype='text/plain')

def logr(host, level, msg):
        req_str = (''.join(['http://',LOGR_HOST,':5002',
                   '/add?moment=',str(datetime.now()),
                   '&host=',host,
                   '&level=',level,
                   '&msg=',msg
                  ]))
        req = requests.get(req_str)
