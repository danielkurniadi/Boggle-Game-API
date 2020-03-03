#!/usr/bin/env bash

# RUN APP
docker run --name boggleapi \
 -d -p 5001:9001 --rm \
 -e DATABASE_URI=mongodb://mongoserver:27017/testdb \
 --link mongo:mongoserver \
 boggleapi:latest
