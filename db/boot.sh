#!/bin/sh
export FLASK_APP=db.py
# for docker:
#export LOGR_HOST="172.17.0.1"
# for k8s:
export LOGR_HOST=logr-service
flask run --host=0.0.0.0 --port=7000
