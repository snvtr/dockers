#!/bin/sh
export FLASK_APP=logr.py
echo "--" > log
flask run --host=0.0.0.0 --port=5002

