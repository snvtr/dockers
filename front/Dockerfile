FROM python:latest

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY front.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP front.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]