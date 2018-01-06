# docker-django2

This is for creating django2 enviroment

Tech stack is

- django2

- elasticsearch

- fluentd

- gunicorn

- kibana

- nginx

- postgres

- python3

- redis

# Consideration for production usage

DB must be separated and should not use docker version. Ideally you should use DBAAS

# File which should be edited for customization

Though the system can work just by

```
git clone git@github.com:hikarine3/docker-django2.git;
cd docker-django2;
docker-compose up -d;
```

it is just default and you should do some customization after you confirmed the system work without problem.

If you want to use postgresql instead of sqlite

```
vi env_example
```

```
vi sql/create_database.sql
```

```
vi nginx/site-enabled/default
```

```
rm -rf djangopj/*
```
and put django's content

# How to use

## To start

```
docker-compose up
```

# Rebuild

```
docker-compose build --no-cache
```

# URL which you can confirm

## Web server
http://localhost/


## Kibana
http://localhost:5601/

# For real usage

djangopj

is the folder for the source code of django

If you want to put your own django PJ,

```
rm -rf djangopj/*
```

and put your django PJ sour code under djangopj/

# License

MIT

# Author

Hajime Kurita

An adminstrator of https://sakuhindb.com/ , http://minakoe.jp/ and so on

https://twitter.com/hikarine3

https://en.sakuhindb.com/pe/Administrator/
