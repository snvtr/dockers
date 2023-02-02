#!/bin/sh
export FLASK_APP=front.py
# for docker:
#export BACK_HOST="172.17.0.1"
#export LOGR_HOST="172.17.0.1"
# for k8s:
export BACK_HOST=back-service
export LOGR_HOST=logr-service
flask run --host=0.0.0.0 --port=5000
