FROM python:3.8-alpine

RUN adduser -D api

WORKDIR /home/api

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bit/pip install gunicorn

COPY app app
COPY migrations migrations
COPY api.py config.py boot.sh ./
RUN chmod -x boot.sh

ENV FLASK_APP=api.py

RUN chown -R api:api ./
USER api

EXPOSE 5000
ENTRYPOINT ["./boot.sh"] 