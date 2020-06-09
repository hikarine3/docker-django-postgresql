FROM centos
MAINTAINER Hajime Kurita

# Setup
RUN yes | rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY*
RUN yes | dnf install epel-release
RUN yes | dnf update
RUN yes | dnf install python3
RUN yes | dnf install libpq-devel
RUN yes | dnf install python3-devel

RUN yes | dnf module disable postgresql;
RUN yes | dnf install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm;
RUN yes | dnf -y install postgresql12;
RUN yes | dnf -y install postgresql12-devel;
RUN yes | dnf install gcc;

RUN python3 -m pip install --user --upgrade pip
RUN python3 -m pip install django
RUN python3 -m pip install django-environ
RUN python3 -m pip install gunicorn
RUN python3 -m pip install psycopg2

ENV PJ djangopj
RUN mkdir -p /var/www/$PJ
WORKDIR /var/www/$PJ
COPY $PJ /var/www/$PJ
RUN mkdir -p /var/www/$PJ/static/admin

ENV PYTHONUNBUFFERED 1
