#!/bin/sh
export FLASK_APP=db.py
export LOGR_HOST=$(ip -br a | grep UP | awk '{print $3}' | sed -r 's/\/\w+//')
flask run --host=0.0.0.0 --port=7000