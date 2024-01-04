# 特徴
管理画面が標準装備、しかも自動生成  
 モデルを作成すると自動的に管理画面に追加される  
 CSVのインポート/エクスポート機能や検索入力でオートコンプリートなどのユーザカスタムも自由度が高い  
ユーザ認証機能が標準装備なのでセキュリティが高い  
 ユーザカスタムも可能、OAuth2のカスタムを入れてgoogle辺りと連携とかも簡単  
 グループの概念も標準で装備してるので運用が楽  
 URL単位でアクセス制御もできるし、管理画面ではモデル単位で参照/追加/変更/削除の制御も可能  
Ptythonの超豊富なライブラリを利用できる  
 みんなで巨人の肩に乗ろう！他の言語にあってPythonに無いライブラリとか存在しないと思うよ  
 AIって言えばPythonだよね！ってところもあるし、この辺利用したサービス開発するのも親和性が高くて良い  
フルスタックフレームワークなのでフロントからバックエンドまでDjangoだけで出来る  
 まー、社内システムならともかく外部に出すならフロントは別で作るけどね、それでもデモ版を素早くリリース出来るのは良い  
学習コストが低い  
 フレームワークの構造が単純で理解しやすく、独自の書き方みたいなものは比較的少ないので開発参加への敷居が低い  
保守と運用が楽  
 開発コストと学習コストが低いので  
コミュニティ情報が豊富  
 基本英語にはなるけどコミュニティの規模が大きくて活発なので情報収集に困る事は無い、ググれば解決の安心感  

Ninjaは?  
OpenAPIが標準装備、モチロン自動生成  


# pythonの仮想環境を作成

まずはPythonの開発環境を構築して行くよ

## 作業ディレクトリ内で早速仮想環境
```
zagan@LarkBoxX:~/development/juke_box$ python3.10 -m venv venv3.10
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/zagan/development/juke_box/venv3.10/bin/python3.10
```

## なんか怒られたのでvenvを別途入れる
pythonインストールすると標準で入ってる場合が多いんだけどね
```
zagan@LarkBoxX:~/development/juke_box$ sudo apt install python3.10-venv
[sudo] password for zagan: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-distutils python3-lib2to3 python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-distutils python3-lib2to3 python3-pip-whl python3-setuptools-whl python3.10-venv
0 upgraded, 5 newly installed, 0 to remove and 23 not upgraded.
Need to get 2690 kB of archives.
After this operation, 4056 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-lib2to3 all 3.10.8-1~22.04 [77.6 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-distutils all 3.10.8-1~22.04 [139 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-pip-whl all 22.0.2+dfsg-1ubuntu0.4 [1680 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-setuptools-whl all 59.6.0-1.2ubuntu0.22.04.1 [788 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3.10-venv amd64 3.10.12-1~22.04.2 [5724 B]
Fetched 2690 kB in 4s (723 kB/s)     
Selecting previously unselected package python3-lib2to3.
(Reading database ... 28607 files and directories currently installed.)
Preparing to unpack .../python3-lib2to3_3.10.8-1~22.04_all.deb ...
Unpacking python3-lib2to3 (3.10.8-1~22.04) ...
Selecting previously unselected package python3-distutils.
Preparing to unpack .../python3-distutils_3.10.8-1~22.04_all.deb ...
Unpacking python3-distutils (3.10.8-1~22.04) ...
Selecting previously unselected package python3-pip-whl.
Preparing to unpack .../python3-pip-whl_22.0.2+dfsg-1ubuntu0.4_all.deb ...
Unpacking python3-pip-whl (22.0.2+dfsg-1ubuntu0.4) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_59.6.0-1.2ubuntu0.22.04.1_all.deb ...
Unpacking python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
Selecting previously unselected package python3.10-venv.
Preparing to unpack .../python3.10-venv_3.10.12-1~22.04.2_amd64.deb ...
Unpacking python3.10-venv (3.10.12-1~22.04.2) ...
Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
Setting up python3-pip-whl (22.0.2+dfsg-1ubuntu0.4) ...
Setting up python3-lib2to3 (3.10.8-1~22.04) ...
Setting up python3-distutils (3.10.8-1~22.04) ...
Setting up python3.10-venv (3.10.12-1~22.04.2) ...
```

## さ、気を取り直してもう一回
```
zagan@LarkBoxX:~/development/juke_box$ python3.10 -m venv venv3.10
```

## 出来たね？
```
zagan@LarkBoxX:~/development/juke_box$ ls
venv3.10
```

## 早速仮想環境に切り替えてみよう
```
zagan@LarkBoxX:~/development/juke_box$ source venv3.10/bin/activate
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ 
```

## 仮想環境から抜ける
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ deactivate 
zagan@LarkBoxX:~/development/juke_box$ 
```

# django-ninjaの開発環境構築

さて、次は早速Django-ninjaの準備だ  
まずはpipというpythonのパッケージ管理システムからdjango-ninjaをインストールするよ  

## pip経由でdjango-ninja
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ pip install django-ninja
Collecting django-ninja
  Downloading django_ninja-1.0.1-py3-none-any.whl (2.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 15.0 MB/s eta 0:00:00
Collecting Django>=2.2
  Downloading Django-4.2.7-py3-none-any.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 25.3 MB/s eta 0:00:00
Collecting pydantic<3.0.0,>=2.0
  Downloading pydantic-2.5.2-py3-none-any.whl (381 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 381.9/381.9 KB 26.6 MB/s eta 0:00:00
Collecting asgiref<4,>=3.6.0
  Downloading asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.4.4-py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 KB 5.7 MB/s eta 0:00:00
Collecting typing-extensions>=4.6.1
  Using cached typing_extensions-4.8.0-py3-none-any.whl (31 kB)
Collecting annotated-types>=0.4.0
  Downloading annotated_types-0.6.0-py3-none-any.whl (12 kB)
Collecting pydantic-core==2.14.5
  Downloading pydantic_core-2.14.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 27.4 MB/s eta 0:00:00
Installing collected packages: typing-extensions, sqlparse, annotated-types, pydantic-core, asgiref, pydantic, Django, django-ninja
Successfully installed Django-4.2.7 annotated-types-0.6.0 asgiref-3.7.2 django-ninja-1.0.1 pydantic-2.5.2 pydantic-core-2.14.5 sqlparse-0.4.4 typing-extensions-4.8.0
```

## django-ninjaのフレームワークを使ってプロジェクトを作成する
現在いるディレクトリ直下に作成したいので最後のドットを忘れずに！
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ django-admin startproject juke_box .
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ ls
juke_box  manage.py  venv3.10
```


# サービスを起動して見る

プロジェクトを作成したらまずやって見ることは？  
そう！アクセスして見たいよね！早速やってみよう！  

## サービスを起動する
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 26, 2023 - 13:52:02
Django version 4.2.7, using settings 'juke_box.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

なんか怒られてるね？気にせずブラウザでアクセスして見よう  
http://127.0.0.1:8000/ だね  
私の場合はリモートの開発マシンの 192.168.1.5 でポート変換して実行しているので http://192.168.1.5/ になる  
[01]  
エラー画面が表示されたね？  
これはDjangoが表示しているエラー画面だ、これから頻繁に見る事になる  
ALLOWED_HOSTS に 192.168.1.5が無いぞって言われてるね、分かりやすい！  

設定ファイルを変更してやろう  
ALLOWED_HOSTS に 192.168.1.5 を追加してやる  
$ vi juke_box/settings.py  
```
ALLOWED_HOSTS = ['192.168.1.5']

```

さぁもう一度ブラウザで開いて見て  
[02]  
うん！最高の気分だね！  

# DBセットアップ

でもまだもう一つやらなきゃいけない事がある  
サービスを起動した時に何か怒られていたね？  
```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
そう、ここだ、マイグレーションを実行しろって書かれてる  
要するにDBに予め入れなきゃいけないデータがあるので実行する必要があるって事だ  
  
今回は面倒なのでDockerでPostgreSQLを入れるよ、MySQLなんかクソさ！(個人の見解です)  
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ docker run -d --name juke_box_postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres:14.10
Unable to find image 'postgres:14.10' locally
14.10: Pulling from library/postgres
1f7ce2fa46ab: Pull complete 
2ed24675225e: Pull complete 
3e7e114d75ac: Pull complete 
da4f8c31b25f: Pull complete 
0088c457041b: Pull complete 
4e6632acf788: Pull complete 
dc33a1c44da0: Pull complete 
62c7ff97eb13: Pull complete 
21c562472f86: Pull complete 
15cbc10a74f7: Pull complete 
988992fc5bd0: Pull complete 
d5bc21a2dde7: Pull complete 
50e5d260fca3: Pull complete 
Digest: sha256:2cc52135f21efd56a27258fedbbc34c2699b4e28454dc0a7609a1d8adab94f76
Status: Downloaded newer image for postgres:14.10
3dad2ef14f2e0c37245f7a53b92ae01c855c06dbedb36176c7644e0628d68e4c
```

dockerを確認して見よう  
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS                 PORTS                    NAMES
3dad2ef14f2e   postgres:14.10       "docker-entrypoint.s…"   20 seconds ago   Up 18 seconds          0.0.0.0:5432->5432/tcp   juke_box_postgres
```

postgresのクライアントをインストールしよう
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ sudo apt install postgresql-client-common
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  postgresql-client-common
0 upgraded, 1 newly installed, 0 to remove and 23 not upgraded.
Need to get 29.6 kB of archives.
After this operation, 194 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 postgresql-client-common all 238 [29.6 kB]
Fetched 29.6 kB in 2s (13.9 kB/s)                   
Selecting previously unselected package postgresql-client-common.
(Reading database ... 28889 files and directories currently installed.)
Preparing to unpack .../postgresql-client-common_238_all.deb ...
Unpacking postgresql-client-common (238) ...
Setting up postgresql-client-common (238) ...
Processing triggers for man-db (2.10.2-1) ...

(venv3.10) zagan@LarkBoxX:~/development/juke_box$ sudo apt install postgresql-client-14
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libpq5
Suggested packages:
  postgresql-14 postgresql-doc-14
The following NEW packages will be installed:
  libpq5 postgresql-client-14
0 upgraded, 2 newly installed, 0 to remove and 23 not upgraded.
Need to get 1362 kB of archives.
After this operation, 4325 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpq5 amd64 14.9-0ubuntu0.22.04.1 [141 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 postgresql-client-14 amd64 14.9-0ubuntu0.22.04.1 [1222 kB]
Fetched 1362 kB in 4s (388 kB/s)               
Selecting previously unselected package libpq5:amd64.
(Reading database ... 28926 files and directories currently installed.)
Preparing to unpack .../libpq5_14.9-0ubuntu0.22.04.1_amd64.deb ...
Unpacking libpq5:amd64 (14.9-0ubuntu0.22.04.1) ...
Selecting previously unselected package postgresql-client-14.
Preparing to unpack .../postgresql-client-14_14.9-0ubuntu0.22.04.1_amd64.deb ...
Unpacking postgresql-client-14 (14.9-0ubuntu0.22.04.1) ...
Setting up libpq5:amd64 (14.9-0ubuntu0.22.04.1) ...
Setting up postgresql-client-14 (14.9-0ubuntu0.22.04.1) ...
update-alternatives: using /usr/share/postgresql/14/man/man1/psql.1.gz to provide /usr/share/man/man1/psql.1.gz (psql.1.gz) in auto mode
Processing triggers for libc-bin (2.35-0ubuntu3.4) ...
```

アクセスして見よう
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ psql -h localhost -p 5432 -U postgres
Password for user postgres: 
psql (14.9 (Ubuntu 14.9-0ubuntu0.22.04.1), server 14.10 (Debian 14.10-1.pgdg120+1))
Type "help" for help.

postgres=# create database juke_box;
CREATE DATABASE

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 juke_box  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# \q
```

大丈夫そうだね！  
  
設定ファイルを書き換えよう  
$ vi juke_box/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘juke_box’,
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

djangoがpythonにアクセスするためのライブラリ
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 25.5 MB/s eta 0:00:00
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.9

(venv3.10) zagan@LarkBoxX:~/development/juke_box$ sudo apt install libpq-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libssl-dev
Suggested packages:
  postgresql-doc-14 libssl-doc
The following NEW packages will be installed:
  libpq-dev libssl-dev
0 upgraded, 2 newly installed, 0 to remove and 23 not upgraded.
Need to get 2520 kB of archives.
After this operation, 13.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libssl-dev amd64 3.0.2-0ubuntu1.12 [2373 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpq-dev amd64 14.9-0ubuntu0.22.04.1 [147 kB]
Fetched 2520 kB in 4s (709 kB/s)    
Selecting previously unselected package libssl-dev:amd64.
(Reading database ... 29194 files and directories currently installed.)
Preparing to unpack .../libssl-dev_3.0.2-0ubuntu1.12_amd64.deb ...
Unpacking libssl-dev:amd64 (3.0.2-0ubuntu1.12) ...
Selecting previously unselected package libpq-dev.
Preparing to unpack .../libpq-dev_14.9-0ubuntu0.22.04.1_amd64.deb ...
Unpacking libpq-dev (14.9-0ubuntu0.22.04.1) ...
Setting up libssl-dev:amd64 (3.0.2-0ubuntu1.12) ...
Setting up libpq-dev (14.9-0ubuntu0.22.04.1) ...
Processing triggers for man-db (2.10.2-1) ...
```

さぁマイグレーションして見よう

```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

そして起動
```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 26, 2023 - 15:29:16
Django version 4.2.7, using settings 'juke_box.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

怒られなくなったね  
http://127.0.0.1/admin/ にアクセスして見よう  
[03]  
そう！管理画面だ！しかしユーザが存在しないのでコマンドラインで作成する必要がある  

```
(venv3.10) zagan@LarkBoxX:~/development/juke_box$ ./manage.py createsuperuser
Username (leave blank to use 'zagan'): 
Email address: zagan.the.gun@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

ここで作成したユーザIDとパスワードを使って管理画面にアクセスして見よう  
[04]  
おめでとう！これで君の開発環境はほぼ全て整った！  
  
この管理画面ではプロジェクトで作成したテーブルを直接 追加/変更/削除 する事が出来る  
他にも直接このページの各項目をカスタマイズする事も出来るよ  

# サービス作成

## テストAPI作成
まずは手っ取り早く動くところが見たい！
以下のファイルを下図のように変更しよう
$ vi juke_box/urls.py
```
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
```
編集が終わったら早速ブラウザでアクセスして見よう
http://192.168.1.5/api/add?a=1&b=2  
[05]  
やったぜ！  

## swagger確認
DjangoNinjaはなんとSwaggerが標準装備、モチロン自動生成だ  
http://192.168.1.5/api/docs/ にアクセスして見よう  
[06]  
APIを作成した場合はここで直接テストも出来るので開発が非常に捗る！  
[07]  

## アプリケーションの作成
```
$ ./manage.py startapp apis
```

## モデル作成
```
$ vi apis/models.py
$ ./manage.py makemigrations
Migrations for 'apis':
  apis/migrations/0001_initial.py
    - Create model Joints
$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, apis, auth, contenttypes, sessions
Running migrations:
  Applying apis.0001_initial... OK
```

## スキーマ作成

## API作成

## swagger確認


