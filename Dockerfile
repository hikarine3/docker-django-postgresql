FROM alpine
MAINTAINER Hajime Kurita

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base

RUN pip3 install --upgrade pip
RUN pip3 install django django-environ gunicorn psycopg2
RUN apk del -r python3-dev postgresql

ENV PJ djangopj
RUN mkdir -p /var/www/$PJ
WORKDIR /var/www/$PJ
COPY $PJ /var/www/$PJ
RUN mkdir -p /var/www/$PJ/static/admin

ENV PYTHONUNBUFFERED 1
