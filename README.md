# Radic Prometheus Dashboard

## Introduction
This repository includes a Docker Compose stack that we use to request data from our API with a Python script, store the data with Prometheus, and then output it to a Grafana interface.

## Installation
```
git clone https://github.com/Primexz/RadicGraph
cd RadicGraph
docker-compuse up -d
```
Open on your host: http://localhost:3000
> Default Grafana crendentails are admin:admin