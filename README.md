# docker-django-postgresql

This is for creating django's miminum docker enviroment

Tech stack is

- django 3.x

- gunicorn

- nginx

- postgresql

- python 3.x

You can start python's project using this docker environment for local development.

And you can deploy your code to production just by synching the code or using docker same way.

# How to use

Template is provided through

https://github.com/hikarine3/docker-django-postgresql

so click "Use this template" and start your project from there.

Then git clone your repository to your environment and start docker.

Example

```
git clone git@github.com:hikarine3/docker-django-postgresql.git;
cd docker-django-postgresql;
docker-compose up -d;
```

You should be able to see web site at
http://localhost/

You can connect to postgresql server by
```
docker exec -i -t `docker ps|grep postgres:latest|awk '{print $1}'`  psql  --user postgres
```

Log in to web server
```
docker exec -i -t `docker ps|grep docker-django-postgresql_web|awk '{print $1}'` /bin/bash;
```

To get installed python's library list, you can get it by typing
```
docker exec -i -t `docker ps|grep docker-django-postgresql_web|awk '{print $1}'` pip freeze;
```

# Customization

If you want to use postgresql instead of sqlite,
create user on postgresql and define connection information in djangopj/djangopj/settings.py by modifying value of DATABASES=... value.

exmple
```
# postgres1 is container name of postgresql server
HOSTADDRESS = "postgres1"
HOSTPORT = 5432
DBNAME = "..."
DBUSER = "..."
DBUSERPASS = "..."
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBUSERPASS,
        'HOST': HOSTADDRESS,
        'PORT': HOSTPORT
    }
}
```

Of course, you have to create database and user to access to db with the credentials.

```
CREATE DATABASE $DATABASE;

CREATE USER $USERID PASSWORD $PASSWORD;

GRANT ALL ON DATABASE $DATABASE TO $USERID;

```

# Guidance of constructing Django

- JP: https://vpshikaku.com/django%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab-%e8%a8%ad%e5%ae%9a-%e9%96%8b%e7%99%ba%e6%96%b9%e6%b3%95/

# License

MIT

# Author

## Name
Hajime Kurita

## Twitter
- EN: https://twitter.com/hajimekurita
- JP: https://twitter.com/hikarine3

## Weibo
- CN: https://www.weibo.com/hajimekurita

## Corporation page
- CN: https://1stclass.co.jp/en/
- EN: https://1stclass.co.jp/en/
- JP: https://1stclass.co.jp/

## Techincoal web services
### VPS & Infra
- CN: https://vpsranking.com/zh/
- EN: https://vpsranking.com/en/
- JP: https://vpshikaku.com/

### Programming
- EN: https://programminglang.com/en/
- CN: https://programminglang.com/zh/
- JP: https://programminglang.com/ja/

### PSS
- Docker: https://hub.docker.com/u/1stclass/
- Github: https://github.com/hikarine3
- NPM: https://www.npmjs.com/~hikarine3
- Perl: http://search.cpan.org/~hikarine/
- PHP: https://packagist.org/packages/hikarine3/
- Python: https://pypi.org/user/hikarine3/
