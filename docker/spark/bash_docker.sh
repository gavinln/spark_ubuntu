#!/bin/bash

sudo docker exec -t -i $(sudo docker ps -lq) /bin/bash -c "cd /usr/local/spark;bash"
