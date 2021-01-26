# Catalog



## 1. Prerequisites
Устанавливаем требуемые пакеты
```bash
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl pipenv supervisor
```
Переходим в директорию Django-проекта
```bash
git clone https://github.com/CarolusXII/sperma -b backend-app
cd catalog_app
```
Устанавливаем зависимости
```
pipenv sync
pipenv shell
```

## 2. Running development server
Запускаем базу
```bash
sudo service postgresql start
```
Даем доступ текущему UNIX пользователю к psql и команде createdb
```bash
sudo -u postgres createuser --superuser $USER
sudo -u postgres createdb $USER
```
Создаем базу
```bash
createdb $YOUR_DB_NAME
```
Запускаем миграции
```
python manage.py makemigrations
python manage.py migrate
```
Запускаем сервер разработки
```bash
python manage.py runserver # 127.0.0.1:8000
```

## 3. Running production server
### 3.1 Configure supervisor
Даем права bash-скрипту, который стартует gunicorn
```bash
chmod +x /home/grum231/prog/python/bin/gunicorn_start.sh
```
Создаем файл конфига
```bash
sudo vim /etc/supervisor/conf.d/catalog.conf
```
Пример файла конфига supervisor
```conf
[program:gunicorn]
# command - путь до bash-скрипта, запускающего gunicorn
command=/home/grum231/prog/python/bin/gunicorn_start.sh
user=grum231
process_name=%(program_name)s
numproc=1
autostart=true
autorestart=true
redirect_stderr=true
```
Запускаем supervisor
```bash
sudo service supervisor start
```

## 4. Запускаем nginx
```bash
sudo service nginx start
sudo vim /etc/nginx/sites-enabled/default
```
Пример конфига nginx
```conf
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                proxy_pass       http://127.0.0.1:8002;
                proxy_set_header X-Forwarded-For $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header       P3P 'CP="ALL DSP CPR PSAa PSDa OUR NOR ONL UNI COM NAV"';
                add_header       Access-Control-Allow-Origin *;
        }
}
```
Перезапускаем nginx
```bash
sudo service nginx restart
```
## 5. Если не подключается по публичному IP
Т. к. запускалось это все на ВМ Oracle Cloud, то я открыл 80 порт в правилах входа 
![](https://i.ibb.co/ZMyqrhb/photo5219673914198832611.jpg)

и iptables в консоли, после этого все должно исправно работать
```bash
sudo iptables -I INPUT 2 -p tcp --dport 80 -j ACCEPT
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```