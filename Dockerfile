FROM centos
MAINTAINER Hajime Kurita

# Setup
RUN yes | rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY*
RUN yes | dnf install epel-release
RUN yes | dnf update
RUN yes | dnf install python3
RUN yes | dnf install postgresql
RUN yes | dnf install libpq-devel
RUN yes | dnf install python3-devel
RUN yes | dnf install postgresql
RUN yes | dnf install postgresql-devel
RUN yes | dnf install gcc

RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install django-environ
RUN pip3 install gunicorn
RUN pip3 install psycopg2

ENV PJ djangopj
RUN mkdir -p /var/www/$PJ
WORKDIR /var/www/$PJ
COPY $PJ /var/www/$PJ
RUN mkdir -p /var/www/$PJ/static/admin

ENV PYTHONUNBUFFERED 1
