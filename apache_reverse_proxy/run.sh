#! /bin/bash

cd ./acme.sh
./acme.sh --install \
          -m my@example.com \
          --home /usr/local/.acme.sh

cd /usr/local/.acme.sh

./acme.sh --issue \
          -d matiiss.com \
          -d www.matiiss.com \
          -w /usr/local/ssl

./acme.sh --installcert \
          -d matiiss.com \
          -d www.matiiss.com \
          --certpath /usr/local/ssl/matiiss.com.pem \
          --keypath /usr/local/ssl/matiiss.com.key \
          --capath /usr/local/ssl/matiiss.com.pem \
          --reloadcmd "systemctl restart apache2"
          
cd /usr/local

httpd-foreground