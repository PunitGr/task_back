# task_back

## Basic Setup
```
git clone git@github.com:PunitGr/task_back.git
cd task_back
sudo easy_install pip
pip install virtualenv
pip install virtualenvwrapper
source virtualenvwrapper.sh
mkvirtualenv --python=/usr/local/bin/python3 instawork
```

## Install packages
```
workon instawork
(instawork)$ pip install -r requirements.txt
```

## Setup DB

Please install and setup mysql server first and start mysql server with `mysql.server start`.

Log in to mysql server using `mysql -u root -p`. After logging in,

```
CREATE DATABASE task_back;
CREATE USER 'instawork'@'localhost' IDENTIFIED BY 'instawork';
GRANT ALL PRIVILEGES ON task_back.* TO 'instawork'@'localhost';
quit
```

## Start django server
```
workon instawork
(instawork)$./manage.py migrate
(instawork)$./manage.py runserver
```
The server will be live on [http://localhost:8000/](http://localhost:8000/).

## Run tests
To run tests first create test database,
Log in to mysql server using `mysql -u root -p`. After logging in,

```
CREATE DATABASE test_task_back;
GRANT ALL PRIVILEGES ON test_task_back.* TO 'instawork'@'localhost';
```

## Documentation
Read the docs, [here](/Docs.md)
