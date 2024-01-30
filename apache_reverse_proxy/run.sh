echo "hi"
acme.sh/acme.sh --install -m my@example.com
echo "hi 2"
acme.sh/acme.sh --issue --standalone -d matiiss.com -d www.matiiss.com
echo "hi 3"
acme.sh/acme.sh --installcert  -d matiiss.com -d www.matiiss.com \
                --certpath /usr/local/ssl/matiiss.com.pem \
                --keypath /usr/local/ssl/matiiss.com.key \
                --capath /usr/local/ssl/matiiss.com.pem \
                --reloadcmd "systemctl restart apache2"
echo "hi 4"

httpd-foreground