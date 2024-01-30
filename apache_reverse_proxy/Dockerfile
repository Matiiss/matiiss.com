FROM httpd:2.4

WORKDIR /usr/local

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./httpd.conf.d /usr/local/apache2/conf/httpd.conf.d

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN git clone --depth 1 https://github.com/acmesh-official/acme.sh.git

COPY ./run.sh .

CMD ["./run.sh"]
