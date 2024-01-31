#!/bin/bash

mkdir /htdocs
cp -r flask_app/static/. /htdocs

gunicorn -w 4 -b 0.0.0.0:8000 flask_app:app
