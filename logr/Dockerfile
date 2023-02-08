FROM ubuntu:latest 

RUN apt update && apt install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY logr.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP logr.py

EXPOSE 5002
ENTRYPOINT ["./boot.sh"]
