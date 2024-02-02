FROM nginx:latest

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./conf.d /etc/nginx/conf.d

EXPOSE 80 443

ENTRYPOINT [ "/bin/bash" ]
CMD sleep 20s && /docker-entrypoint.sh nginx -g daemon off;
