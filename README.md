# docker-django2
This is for creating django2 enviroment
Tech stack is
python3
django2
elasticsearch
fluentd
kibana
nginx
postgres
redis

# Consideration for production usage
- DB must be separated and should not use docker version. Ideally you should use DBAAS

# File which should be edited for customization

Though you can edit docker/web/django/env_example, best way is to create new .env file 

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

# Prerequisistes

```
mkdir -p ~/data/docker/psql
```

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
