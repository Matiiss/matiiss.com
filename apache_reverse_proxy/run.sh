#! /bin/bash

acme.sh/acme.sh --install \
                --standalone \
                -m my@example.com \
                --home /usr/local
                
acme.sh/acme.sh --issue \
                -d matiiss.com \
                -d www.matiiss.com

acme.sh/acme.sh --installcert \
                -d matiiss.com \
                -d www.matiiss.com \
                --certpath /usr/local/ssl/matiiss.com.pem \
                --keypath /usr/local/ssl/matiiss.com.key \
                --capath /usr/local/ssl/matiiss.com.pem \
                --reloadcmd "systemctl restart apache2"

httpd-foreground