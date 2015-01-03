Install snakebite (Python hdfs client)
pip install snakebite

Display IP address
sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' $(sudo docker ps -lq)

Use IP address from above to get information about the file system
snakebite -n 172.17.0.51 -p 9000 df -h

To start Spark master
1. Change to the Spark directory
cd /usr/local/spark

2. Start Master
/usr/local/spark/sbin/start-master.sh -h 0.0.0.0 -p 7077

3. Start slave
/usr/local/spark/sbin/start-slave.sh 2 spark://a8a87ff1a9fb:7077

4. Start shell
/usr/local/spark/bin/pyspark --master spark://a8a87ff1a9fb:7077

5. Stop slaves
/usr/local/spark/sbin/stop-slaves.sh

6. Stop Master
/usr/local/spark/sbin/stop-master.sh




