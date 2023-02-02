#!/bin/bash

cd back
docker build . -t back:local
cd ../db
docker build . -t db:local
cd ../front
docker build . -t front:local
cd ../logr 
docker build . -t logr:local
