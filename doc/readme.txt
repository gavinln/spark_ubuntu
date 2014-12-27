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
./sbin/start-master.sh -i 127.0.0.1 -p 7077

3. Start slave
./sbin/start-slave.sh 1 spark://92faf3819eb6:7077

4. Start shell
./bin/pyspark --master spark://92faf3819eb6:7077

5. Stop slaves
./sbin/stop-slaves.sh

6. Stop Master
./sbin/stop-master.sh




