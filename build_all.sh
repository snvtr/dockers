#!/bin/bash

cd back
docker build . -t back
cd ../db
docker build . -t db
cd ../front
docker build . -t front
cd ../logr 
docker build . -t logr
