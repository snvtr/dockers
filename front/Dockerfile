FROM ubuntu:latest

RUN apt update && apt install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY front.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP front.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
