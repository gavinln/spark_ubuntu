Install snakebite (Python hdfs client)
pip install snakebite

Display IP address
sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' $(sudo docker ps -lq)

Use IP address from above to get information about the file system
snakebite -n 172.17.0.51 -p 9000 df -h


