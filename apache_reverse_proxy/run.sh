#! /bin/bash

cd ./acme.sh
./acme.sh --install \
          -m matiiss@matiiss.com \
          --home /usr/local/.acme.sh

cd /usr/local/.acme.sh

./acme.sh --issue \
          -d matiiss.com \
          -d www.matiiss.com \
          --standalone \
          --keylength ec-256 \
          --debug

./acme.sh --installcert \
          -d matiiss.com \
          -d www.matiiss.com \
          --cert-file /usr/local/apache2/htdocs/matiiss.com.pem \
          --key-file /usr/local/apache2/htdocs/matiiss.com.key \
          --fullchain-file /usr/local/apache2/htdocs/fullchain.pem \
          --reloadcmd "systemctl restart apache2" \
          --debug

cd /usr/local

httpd-foreground