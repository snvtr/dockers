#!/bin/sh
export FLASK_APP=back.py
# for docker:
#export LOGR_HOST=$(ip -br a | grep UP | awk '{print $3}' | sed -r 's/\/\w+//')
#export DB_HOST=$(ip -br a | grep UP | awk '{print $3}' | sed -r 's/\/\w+//')
# for k8s:
export LOGR_HOST=logr-service
export DB_HOST=db-service
flask run --host=0.0.0.0 --port=5001

