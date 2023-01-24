FROM python:latest

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY logr.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP logr.py

EXPOSE 5002
ENTRYPOINT ["./boot.sh"]