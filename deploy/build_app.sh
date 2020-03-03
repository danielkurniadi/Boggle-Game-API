#!/usr/bin/env bash

# BUILD
docker build -t boggleapi:latest \
 --build-arg PORT=9001 \
 --build-arg ENV=test \
 --build-arg HOST=0.0.0.0 \
 --build-arg DEBUG=1 \
 --build-arg ENV=test \
 -f deploy/Dockerfile .
