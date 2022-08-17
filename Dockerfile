FROM python:3.7.13-alpine3.16 

WORKDIR /profiles-rest-api

RUN pip3 install virtualenv
RUN virtualenv env

COPY requirements.txt requirements.txt

RUN source env/bin/activate && pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
