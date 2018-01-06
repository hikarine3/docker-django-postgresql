FROM 1stclass/python3-django2-alpine-base
MAINTAINER Hajime Kurita https://twitter.com/hikarine3/

# Initialize
# So if you put django's project content under $PJ (django) in default, you can make the system work
ENV PJ djangopj
RUN mkdir -p /var/www/$PJ
WORKDIR /var/www/$PJ
COPY $PJ /var/www/$PJ
RUN mkdir -p /var/www/$PJ/static/admin
