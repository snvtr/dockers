#!/bin/bash

docker run -d -p 5000:5000 front
docker run -d -p 5001:5001 back
docker run -d -p 7000:7000 db
docker run -d -p 5002:5002 logr
 
