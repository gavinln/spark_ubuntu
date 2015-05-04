#!/bin/bash

sudo docker exec -t -i $(sudo docker ps -lq) /etc/bootstrap_pyspark.sh
