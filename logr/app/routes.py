from app import app
import urllib.request
import json
import os
from flask import Response, request

#LOGR_HOST = os.environ.get('LOGR_HOST') or 'localhost'

@app.route('/add')
def add():
    if request.args.get('moment') is not None:
        moment = request.args.get('moment')
    else:
        return Response(response='no moment', status=500, mimetype='text/html')

    if request.args.get('host') is not None:
        host = request.args.get('host')
    else:
        return Response(response='no host', status=500, mimetype='text/html')

    if request.args.get('level') is not None:
        level = request.args.get('level')
    else:
        return Response(response='no level', status=500, mimetype='text/html')

    if request.args.get('msg') is not None:
        msg = request.args.get('msg')
    else:
        return Response(response='no msg', status=500, mimetype='text/html')

    with open('/var/log/logr/log', mode='at') as log_f:
        log_f.write('%s %-8s %-8s %s\n' % (moment, host, level, msg))

    return Response(response='Ok', status=200, mimetype='text/html')

@app.route('/show')
def show():
    ret_str = '<html><pre>'
    with open('/var/log/logr/log', mode='rt') as log_f:
        for line in log_f:
            ret_str += line
    ret_str += '</pre></html>'
    return Response(response=ret_str, status=200, mimetype='text/html')
