FROM python:latest

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY db.py config.py app.db boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP db.py

EXPOSE 7000
ENTRYPOINT ["./boot.sh"]