# docker-django2

This is for creating django2's miminum docker enviroment

Tech stack is

- django

- gunicorn

- nginx

- postgresql

- python

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

For postgres, if you have installed postgresql client, you can connect　by
```
docker exec -i -t `docker ps|grep postgres:latest|awk '{print $1}'`  psql  --user postgres
```

# Customization

If you want to use postgresql instead of sqlite,
create user on postgresql and define connection information in djangopj/djangopj/settings.py by modifying value of DATABASES=... value.

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
- EN: https://1stclass.co.jp/en/
- JP: https://1stclass.co.jp/

# Techincoal web services
## VPS & Infra
- EN: https://vpsranking.com/en/
- CN: https://vpsranking.com/zh/
- JP: https://vpshikaku.com/

## Programming
- EN: https://programminglang.com/en/
- CN: https://programminglang.com/zh/
- JP: https://programminglang.com/ja/

## Github
https://github.com/hikarine3
