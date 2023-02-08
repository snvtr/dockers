#!/bin/sh
export FLASK_APP=back.py
# for docker:
#export LOGR_HOST="172.17.0.1"
#export DB_HOST="172.17.0.1"
# for k8s:
export LOGR_HOST=logr-service
export DB_HOST=db-service
flask run --host=0.0.0.0 --port=5001

