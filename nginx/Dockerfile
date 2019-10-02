FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/conf.d/
#RUN mkdir -p /etc/nginx/conf.d/\
#    && ln -s /etc/nginx/conf.d/app.conf /etc/nginx/conf.d/

# RUN mkdir -p /etc/nginx/sites-enabled/\
#     && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/\
#     && rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]