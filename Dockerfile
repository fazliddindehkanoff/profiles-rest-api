FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /profiles-rest-api
COPY requirements.txt /profiles-rest-api/
RUN pip3 install -r requirements.txt
COPY . /profiles-rest-api/