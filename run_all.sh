#!/bin/bash

docker run -d -p 5000:5000 front:local
docker run -d -p 5001:5001 back:local
docker run -d -p 7000:7000 db:local
docker run -d -p 5002:5002 logr:local
 
