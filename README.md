# Python3-docker笔记
# Docker + Django + Nginx + uWSGI + MySQL

![](img/docker.png)


## Start 
```
$ git pull  https://github.com/bluehole333/python3_nginx_uwsgi_django_docker.git
# or  docker-compose up -d 
$ docker-compose up
```

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