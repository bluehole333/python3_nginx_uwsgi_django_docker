# Python3-docker笔记
# Docker + Django + Nginx + uWSGI + MySQL

![](img/docker.png)

# docker-compose
## Start 
```
$ git pull  https://github.com/bluehole333/python3_nginx_uwsgi_django_docker.git
# or docker-compose up -d 
$ docker-compose up
```

## Config
修改env/conf.env对应参数，保存

## Build
```
$ docker-compose build
$ docker-compose build --no-cache       # build without cache
```

## Logs
```
# 查看所有日志
$ docker-compose logs

# 查看指定容器日志
$ docker-compose logs -f [service_name]
```

## Shell
```
# 进入终端
$ docker-compose run [service_name] bash
```

## 删除所有容器
```
$ docker rm $(docker ps -a -q)
```

## 删除所有镜像
```
$ docker rmi $(docker images -q)
```

# docker-compose - Django
## Commands
```
$ docker-compose run uwsgi python manage.py [command]
```

## Makemigrations or Migrate
```
$ docker-compose run uwsgi python manage.py  makemigrations
$ docker-compose run uwsgi python manage.py  migrate
```

## Django shell
```
$ docker-compose run uwsgi python manage.py  shell
```

## Collectstatic
```
$ docker-compose run uwsgi python manage.py collectstatic
```