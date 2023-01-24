cd back
docker build . --tag back:latest
cd ..\db
docker build . --tag db:latest
cd ..\front
docker build . --tag front:latest
cd ..\logr
docker build . --tag logr:latest