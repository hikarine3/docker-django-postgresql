# docker-django-postgresql

## About this document / この文章について / 关于这个仓库

This document is maitained by writing in English, Japanese and Chinese.

この文章は英語・日本語・中国語で併記されていきます。

本文档以英文，日文和中文撰写。
___

## Purpose of this repository / このレポジトリの目的 /  此存储库的用途
[English]

This will help you to start Django's development using PostgreSQL with docker envrionment support.

In addition to binging up django system in default status, this project add some basic functions to help you to start django project.

Here is the list.

- Admin page
- Listing page with pagination function as example
- Load data as example
- User authentification
- Responsive desgin

<img src="doc/img/localhost.png" />

<img src="doc/img/Site_administration_Django_site_admin.png" />

"accounts" and "geo" are added applications to the default django's file structure, so if you don't need it, you can take it off by removing addtion of INSTALLED_APPS in djangopj/settings.py

[日本語]

このレポジトリは、Djangoの開発をPostgreSQLと一緒にDocker環境で開始する為のテンプレートとして役立ちます。

Djangoを初期状態で起動させるだけでなく、以下の機能を追加した状態で起動させます。

- 管理画面
- 例として項目のリストページ(ページネーション機能付き)
- 例としてデータのDBヘの取込み処理
- ユーザー登録・ログイン・ログアウト機能
- レスポンシブデザイン

プロダクションへのデプロイは、ローカルで生成したコードを本番に転送する事でシステムを動かす事も出来ますし、Dockerとして同じように稼働させる事も出来ます。

accountsとgeoがその為に追加されたアプリなので、必要なければdjangopj/settings.pyのINSTALLED_APPSから外して下さい。

<img src="doc/img/localhost.png" />

<img src="doc/img/Site_administration_Django_site_admin.png" />

リモートサーバーでの稼働はDockerとしてのデプロイも出来るでしょうが、唯コードを本番環境に転送して設定する形でも動きます。

[中文]

这将帮助您使用带有docker envrionment支持的PostgreSQL开始Django的开发。

除了以默认状态启动django系统外，该项目还添加了一些基本功能来帮助您启动django项目。

这是清单。

- 管理页面
- 以分页功能为例的列表页面
- 以加载数据为例
- 用户认证
- 响应式设计

<img src="doc/img/localhost.png" />

<img src="doc/img/Site_administration_Django_site_admin.png" />

“ accounts”和“ geo”是将应用程序添加到默认django的文件结构中，因此，如果不需要它，可以通过删除djangopj / settings.py中的INSTALLED_APPS添加来删除它
___

## Tech stack / 技術セット / 技术栈

- OS: AlmaLinux

- django 4.x + gunicorn + python 3

- nginx

- postgresql: 14

[English]

djangopj is default django's folder.

As default database of PostgreSQL, "example" is prepared.

If you want to change it, modify .env.

You can confirm and change credentials to connect to DB in .env.

For production usage, you must change information in .env.

And it is desirable to exclude .env from the registration in git repository for security purpose.

I am offering .env as registered file in git repository just as demonstration and making this work without any configuration by default.

[日本語]

djangopjがdjangoの初期開発用フォルダーになっています。settings.pyの末尾にはPostgreSQLを一旦は何も触らずDjangoと接続した形で使えるようにする為のカスタマイズが追加されています。

Djangoが使うPostgreSQLの初期設定のデータベースはexampleという名前になっています。

接続に必要な情報は
.env
ファイルの中身をご確認下さい。

.envの中身をdockerを立ち上げる前に変更しておけば、作られるデータベースや接続情報も独自のものにする事ができます。

何も変更しないでも動く様にする為このレポジトリでは.envを用意していますが、本番運用では.envファイルはgit repositoryへの登録を外して運用する事が、セキュリティ上お勧めされます。

[中文]

作为 PostgreSQL 的默认数据库，准备了“示例”。

如果要更改它，请修改 .env。

您可以确认和更改凭据以连接到 .env 中的数据库。

对于生产用途，您必须更改 .env 中的信息。

出于安全目的，最好将 .env 从 git 存储库中的注册中排除。

我在 git 存储库中提供 .env 作为注册文件作为演示，默认情况下无需任何配置即可使其工作。

# How to use / どうやって使うか / 如何使用

[English]

Template is provided through

https://github.com/hikarine3/docker-django-postgresql

so click "Use this template" and start your project from there.

Then git clone your repository to your environment and start docker.


```
git clone git@github.com:hikarine3/docker-django-postgresql.git;
cd docker-django-postgresql;
```

If you want to change database name and its credential, change the content of .env before bringing docker containers up.
```
vi .env
```

After you change .env file, 

```
docker-compose up -d;
```

For completion of settings, type
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py migrate;
```

Then load data by typing
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py loaddata geo/fixtures/country.json geo/fixtures/prefecture.json
```

To create the user who can log in admin screen from http://localhost/admin/, type

```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py createsuperuser;
```

Now you can see demo site with data & a loginable user.

http://localhost/

http://localhost/admin/


[日本語]

テンプレートは

https://github.com/hikarine3/docker-django-postgresql

で配布されているので、"Use this template"のボタンを押して、貴方用のPJの開始に使って下さい。

それからgit cloneし、docker環境を立ち上げてください。

```
git clone git@github.com:hikarine3/docker-django-postgresql.git;
cd docker-django-postgresql;
```

作成するデータベース・接続情報をデフォルトから変更したい場合には、Dockerコンテナを以下のコマンドで立ち上げる前に、.envの中身を編集しておいて下さい。
```
vi .env
```

編集が終わってたら

```
docker-compose up -d;
```

それから
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py migrate;
```
と打ってから、デモ用データを
```
python3 manage.py loaddata geo/fixtures/country.json geo/fixtures/prefecture.json
```
と打つ事で初期データを入れる事が出来ます。

それから管理画面 http://localhost/admin/ にログインできるユーザーを作りましょう。

```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py createsuperuser;
```

あとは、

http://localhost/

と

http://localhost/admin/

を確認して、正常にサイトが稼働している事を確認して下さい。



[中文]

通过提供模板

https://github.com/hikarine3/docker-django-postgresql

因此，请点击“使用此模板”，然后从此处开始您的项目。

然后git将您的存储库克隆到您的环境中，然后启动docker。

```
git clone git@github.com：hikarine3 / docker-django-postgresql.git;
cd docker-django-postgresql;
```

如果要更改数据库名称及其凭据，请在启动 docker 容器之前更改 .env 的内容。
```
vi .env
```

更改 .env 文件后，

```
docker-compose up -d;
```

要完成设置，请键入
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py migrate;
```

创建可以登录管理员屏幕的用户

```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py migrate;
```

然后通过键入加载数据
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py loaddata geo/fixtures/country.json geo/fixtures/prefecture.json
```

要创建可以登录管理员屏幕的用户，请键入
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` python3 manage.py createsuperuser;
```

现在您可以看到带有数据和可登录用户的演示站点。

http://localhost/

http://localhost/admin/


# How to connect to PostgreSQL by docker / PostgreSQLへのdockerでのアクセス / 如何通过Docker连接到PostgreSQL
```
docker exec -i -t `docker ps|grep postgres_by_1stclass|awk '{print $1}'`  psql  --user postgres
```

# How to log in to django's application server / Djangoのアプリケーションサーバーへのdockerでのログイン / 如何登录Django的应用程序服务器
```
docker exec -i -t `docker ps|grep django_app_by_1stclass|awk '{print $1}'` /bin/bash;
```

# Recommendation to set alias / ショートカットとしてalias設定の推奨 / 建议设置alias
Docker's command is long, so it is recommended for you to use alias for some of commands.

Example:
```
alias dpsql="docker exec -i -t \`docker ps|grep postgres_by_1stclass|awk '{print \$1}'\`  psql  --user postgres";
```

```
alias dweb="docker exec -i -t \`docker ps|grep django_app_by_1stclass|awk '{print \$1}'\`"
```

# How Django's folder was created / 既に用意されてるdjangoの開発フォルダの作られ方 / Django文件夹的创建方式

```
PJ=djangopj;
django-admin startproject $PJ .;
cd $PJ;
python3 manage.py collectstatic;
```

# Related technical information / 関連技術の役立ち情報 / 相关技术资料

## 日本語(Japanese)
- [Dockerのインストール・設定方法](https://vpshikaku.com/docker/)

- [Djangoのインストール/設定/開発方法](https://vpshikaku.com/django/)

- [PostgreSQLのインストール・設定・使い方](https://vpshikaku.com/postgresql/)

# License / ライセンス / 执照

MIT

# Author / 作者

## Name / 名前 / 全名
Hajime Kurita

## Twitter
- EN: https://twitter.com/hajimekurita
- JP: https://twitter.com/hikarine3

## Weibo
- CN: https://www.weibo.com/hajimekurita

## Corporation page / 会社ページ / 公司页面
- EN: https://1stclass.co.jp/en/
- CN: https://1stclass.co.jp/zh/
- JP: https://1stclass.co.jp/

## Blog
- EN: https://en.sakuhindb.com/pe/Administrator/
- JP: https://sakuhindb.com/pj/6_B4C9CDFDBFCDA4B5A4F3/

## Techincoal web services / 提供してる技術関連Webサービス / Techincoal Web服务
### VPS & Infra comparison / VPS比較 / VPS比较
- EN: https://vpsranking.com/en/
- CN: https://vpsranking.com/zh/
- JP: https://vpshikaku.com/

### Programming Language Comparison / プログラミング言語比較 / 编程语言比较
- EN: https://programminglang.com/en/
- CN: https://programminglang.com/zh/
- JP: https://programminglang.com/ja/

### OSS
- Docker: https://hub.docker.com/u/1stclass/
- Github: https://github.com/hikarine3
- NPM: https://www.npmjs.com/~hikarine3
- Perl: http://search.cpan.org/~hikarine/
- PHP: https://packagist.org/packages/hikarine3/
- Python: https://pypi.org/user/hikarine3/
