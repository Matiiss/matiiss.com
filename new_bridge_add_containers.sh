#!/bin/bash

REVERSE_PROXY_CONTAINER_NAME="apache_reverse_proxy"
FLASK_APP_CONTAINER_NAME="flask_app"
BRIDGE_NAME="net"

while [[ $# -gt 0 ]]; do
    case "$1" in
        -rpn|--reverse-proxy-name)
            REVERSE_PROXY_CONTAINER_NAME="$2"
            shift
            shift
            ;;
        -fpn|--flask-app-name)
            FLASK_APP_CONTAINER_NAME="$2"
            shift
            shift
            ;;
        -bn|--bridge-name)
            BRIDGE_NAME="$2"
            shift
            shift
            ;;
    esac
done

docker network create $BRIDGE_NAME
docker network connect $REVERSE_PROXY_CONTAINER_NAME
docker network connect $FLASK_APP_CONTAINER_NAME
