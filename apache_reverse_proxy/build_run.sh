#!/bin/bash

IMAGE_NAME="apache_reverse_proxy"
CONTAINER_NAME="apache_reverse_proxy"
PORT="80"

while [[ $# -gt 0 ]]; do
    case "$1" in
        -in|--image-name)
            IMAGE_NAME="$2"
            shift
            shift
            ;;
        -cn|--container-name)
            CONTAINER_NAME="$2"
            shift
            shift
            ;;
        -p|--port)
            PORT="$2"
            shift
            shift
            ;;
    esac
done

docker build -t $IMAGE_NAME .
docker run -d --name $CONTAINER_NAME -p $PORT:80 $IMAGE_NAME
