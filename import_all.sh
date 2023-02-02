#!/bin/bash

microk8s ctr image import front.tar
microk8s ctr image import back.tar
microk8s ctr image import logr.tar
microk8s ctr image import db.tar

