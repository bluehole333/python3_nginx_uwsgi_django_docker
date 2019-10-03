FROM python:3
ENV PYTHONUNBUFFERED 1

# init
RUN mkdir -p /var/www/webapp
WORKDIR /var/www/webapp

# Uwsgi conf
ADD uwsgi/uwsgi.ini /etc/uwsgi/uwsgi.ini

# Create django user
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /var/www/webapp

ADD uwsgi/wait-for-it.sh /var/www/webapp

# Pip install
RUN pip install --upgrade pip
ADD uwsgi/requirements.txt /var/www/webapp
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

#ADD webapp /var/www/webapp
