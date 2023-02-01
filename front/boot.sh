#!/bin/sh
export FLASK_APP=front.py
# for docker:
#export BACK_HOST=$(ip -br a | grep UP | awk '{print $3}' | sed -r 's/\/\w+//')
#export LOGR_HOST=$(ip -br a | grep UP | awk '{print $3}' | sed -r 's/\/\w+//')
# for k8s:
export BACK_HOST=back-service
export LOGR_HOST=logr-service
flask run --host=0.0.0.0 --port=5000
