#!/bin/bash

microk8s.kubectl apply -f front-depl.yaml
microk8s.kubectl apply -f back-depl.yaml
microk8s.kubectl apply -f db-depl.yaml
microk8s.kubectl apply -f logr-depl.yaml

microk8s.kubectl apply -f front-service.yaml
microk8s.kubectl apply -f back-service.yaml
microk8s.kubectl apply -f db-service.yaml
microk8s.kubectl apply -f logr-service.yaml
