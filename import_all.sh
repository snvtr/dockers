#!/bin/bash

microk8s ctr image import front.tar && rm front.tar
microk8s ctr image import back.tar  && rm back.tar
microk8s ctr image import logr.tar  && rm logr.tar
microk8s ctr image import db.tar    && rm db.tar

