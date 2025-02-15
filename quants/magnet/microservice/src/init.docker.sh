#!/bin/bash


#chmod +x .init.docker.sh
#sudo ./init.docker.sh
docker build -t quantbacksrc .
#docker build --no-cache -t quantbacksrc .
docker images
docker run -d -p 8000:8000 quantbacksrc

#docker ps
#docker exec -it container_id /bin/bash