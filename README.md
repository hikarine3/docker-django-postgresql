# docker-django2

This is for creating django2's miminum docker enviroment

Tech stack is

- django2

- gunicorn

- nginx

- postgresql

- python3


You can start python's project using this docker environment for local development.

And you can deploy your code to production just by synching the code or using docker same way.

# How to use

Just type
```
git clone git@github.com:hikarine3/docker-django2.git;
cd docker-django2;
docker-compose up -d;
```
for initial.

You should be able to see web site at
http://localhost/

For postgres, if you have installed postgresql client, you can connect　by
```
psql --user=postgres
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

## Corporation page
- EN: https://1stclass.co.jp/en/
- JP: https://1stclass.co.jp/

# Techincoal web services
## VPS & Infra
- EN: https://vpsranking.com/
- JP: https://vpshikaku.com/

## Programming
- EN: https://programminglang.com/en/
- JP: https://programminglang.com/ja/

## Github
https://github.com/hikarine3
