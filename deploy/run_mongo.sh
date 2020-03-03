#!/usr/bin/env bash

# RUN MONGODB SERVER
docker run --name mongodb -d -v ~/data:/data/db --rm \
mongo:latest
