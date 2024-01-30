FROM httpd:2.4

WORKDIR /usr/local

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./httpd.conf.d /usr/local/apache2/conf/httpd.conf.d

COPY ./acme.sh ./acme.sh

COPY ./run.sh .

CMD ["sudo", "./run.sh"]
