#!/usr/bin/env bash
! docker network create -d bridge weather-app-nt > /dev/null 2>&1
export DOCKER_IP="localhost"
make build-docker-dev
make start-dev
