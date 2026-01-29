FROM nginx:latest

COPY ./nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d /etc/nginx/conf.d

EXPOSE 80 443
