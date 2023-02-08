FROM ubuntu:latest

RUN apt update && apt install -y python3-pip 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY db.py app.db boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP db.py

EXPOSE 7000
ENTRYPOINT ["./boot.sh"]
