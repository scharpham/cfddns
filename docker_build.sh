#!/bin/bash
#sudo docker stop sbx_container
#sudo docker rm sbx_container
#sudo docker image rm sbx_image
sudo docker build -t cfddns .
sudo docker compose up -d