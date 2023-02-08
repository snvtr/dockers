#!/bin/bash

cd back
docker build . -t localhost:32000/back:registry
if (( $? == 0 )) ; then docker push localhost:32000/back:registry ; fi
cd ../db
docker build . -t localhost:32000/db:registry
if (( $? == 0 )) ; then docker push localhost:32000/db:registry ; fi
cd ../front
docker build . -t localhost:32000/front:registry
if (( $? == 0 )) ; then docker push localhost:32000/front:registry ; fi
cd ../logr 
docker build . -t localhost:32000/logr:registry
if (( $? == 0 )) ; then docker push localhost:32000/logr:registry ; fi

