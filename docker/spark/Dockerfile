#FROM sequenceiq/hadoop-docker:2.6.0
FROM hadoop_hadoop:latest
MAINTAINER SequenceIQ

RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.1.1-bin-hadoop2.4.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-1.1.1-bin-hadoop2.4 spark
ENV SPARK_HOME /usr/local/spark
RUN mkdir $SPARK_HOME/yarn-remote-client
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client

RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.1.1-bin-hadoop2.4/lib /spark

ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV SPARK_JAR hdfs:///spark/spark-assembly-1.1.1-hadoop2.4.0.jar
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin

ENV HADOOP_PREFIX /usr/local/hadoop
RUN $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

RUN rm /tmp/*.pid

# installing libraries if any - (resource urls added comma separated to the ACP system variable)
RUN cd $HADOOP_PREFIX/share/hadoop/common ; for cp in ${ACP//,/ }; do  echo == $cp; curl -LO $cp ; done; cd -

# altering the core-site configuration
RUN sed s/HOSTNAME/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/core-site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml

RUN service sshd start
RUN $HADOOP_PREFIX/sbin/start-dfs.sh
RUN $HADOOP_PREFIX/sbin/start-yarn.sh

# reduce log messages
RUN cp /usr/local/hadoop/etc/hadoop/log4j.properties /usr/local/hadoop/etc/hadoop/log4j.properties.bak
RUN sed s/hadoop.root.logger=INFO/hadoop.root.logger=WARN/ /usr/local/hadoop/etc/hadoop/log4j.properties.bak > /usr/local/hadoop/etc/hadoop/log4j.properties

# install ipython
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y python-pip
RUN pip install ipython==1.2.1

# Add script to start Spark Python
ADD bootstrap_pyspark.sh /etc/
RUN chmod u+x /etc/bootstrap_pyspark.sh

CMD ["/etc/bootstrap_pyspark.sh"]

EXPOSE 8080 8081
