#!/bin/bash

mkdir /public
cp -r flask_app/static /public

gunicorn -w 4 -b 0.0.0.0:8000 flask_app:app
