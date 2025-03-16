#!/bin/bash
#sudo docker stop cfddns
#sudo docker rm cfddns
#sudo docker image rm cfddns
sudo docker build -t cfddns .
sudo docker compose up -d
docker run --env-file .env cfddns
