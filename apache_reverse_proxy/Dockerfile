FROM httpd:2.4

WORKDIR /usr/local
RUN usermod -d /usr/local root

RUN apt-get -y update; apt-get -y install curl cron git socat

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./httpd.conf.d /usr/local/apache2/conf/httpd.conf.d

RUN git clone https://github.com/acmesh-official/acme.sh
RUN chmod +x ./acme.sh/acme.sh

RUN mkdir ./ssl
COPY ./run.sh .
RUN chmod +x ./run.sh

EXPOSE 443

CMD ["./run.sh"]
