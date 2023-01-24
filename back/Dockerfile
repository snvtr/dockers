FROM python:latest

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY back.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP back.py

EXPOSE 5001
ENTRYPOINT ["./boot.sh"]