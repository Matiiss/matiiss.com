#!/bin/bash

NAME="noname"
TAG="matiiss.com"
VERSION="1.0"
ADDRESS="127.0.0.1"
PORT="8000"

while [[ $# -gt 0 ]]; do
    case "$1" in
        -n|--name)
            NAME="$2"
            shift
            shift
            ;;
        -t|--tag)
            TAG="$2"
            shift
            shift
            ;;
        -v|--version)
            VERSION="$2"
            shift
            shift
            ;;
        -p|--port)
            PORT="$2"
            shift
            shift
            ;;
        -a|--address)
            ADDRESS="$2"
            shift
            shift
            ;;
    esac
end

git pull
docker build -t $NAME/$TAG:$VERSION .
docker run -d -p $ADDRESS:$PORT:8000 $NAME/$TAG:$VERSION
