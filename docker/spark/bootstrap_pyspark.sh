#!/bin/bash

: ${HADOOP_PREFIX:=/usr/local/hadoop}

$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

rm /tmp/*.pid

# installing libraries if any - (resource urls added comma separated to the ACP system variable)
cd $HADOOP_PREFIX/share/hadoop/common ; for cp in ${ACP//,/ }; do  echo == $cp; curl -LO $cp ; done; cd -

# altering the core-site configuration
sed s/HOSTNAME/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/core-site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml


service sshd start
$HADOOP_PREFIX/sbin/start-dfs.sh
$HADOOP_PREFIX/sbin/start-yarn.sh

# reduce log messages
cp /usr/local/hadoop/etc/hadoop/log4j.properties /usr/local/hadoop/etc/hadoop/log4j.properties.bak
sed s/hadoop.root.logger=INFO/hadoop.root.logger=WARN/ /usr/local/hadoop/etc/hadoop/log4j.properties.bak > /usr/local/hadoop/etc/hadoop/log4j.properties

IPYTHON=1 HOME=/root /usr/local/spark/bin/pyspark --master yarn-client
#PYSPARK_PYTHON=python HOME=/root /usr/local/spark/bin/pyspark

#/bin/bash

