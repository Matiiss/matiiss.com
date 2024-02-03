FROM nginx:latest

COPY ./nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d /etc/nginx/conf.d

COPY ./run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 80 443

# ENTRYPOINT [ "/bin/bash" ]
# CMD [ "/run.sh" ]
