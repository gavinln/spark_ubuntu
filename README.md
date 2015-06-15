spark_ubuntu
============

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/spark_ubuntu.git

About
-----

This project provides a [Ubuntu (14.04)][2] [Vagrant][3] Virtual Machine (VM)
with [Docker][4] containers to host [Spark][5].

[2]: http://releases.ubuntu.com/14.04/
[3]: http://www.vagrantup.com/
[4]: https://www.docker.com/
[5]: https://spark.apache.org/

There are [Puppet][6] scripts that automatically install the software when the VM is started.

[6]: http://puppetlabs.com/

Running
-------

1. To start the virtual machine(VM) type

    ```
    vagrant up
    ```

2. Connect to the VM

    ```
    vagrant ssh
    ```

3. Go to the Hadoop Docker container directory

    ```bash
    cd /vagrant/docker/hadoop
    ```

4. Build the Hadoop images

    ```bash
    sudo docker build  -t sequenceiq/hadoop-docker:2.7.0 .
    ```

5. Go to the Spark Docker container directory

    ```bash
    cd /vagrant/docker/spark
    ```

6. Build the Spark image

    ```bash
    sudo docker build --rm -t sequenceiq/spark:1.3.0 .
    ```

7. Run the Spark image

    ```bash
    sudo fig up -d
    ```

8. Start Python spark shell

    ```bash
    ./pyspark_docker.sh
    ```

9. Change to the Spark folder

    ```bash
    cd /usr/local/spark
    ```

10. Create a RDD (Resilient Distributed Dataset)

    ```python
    textFile = sc.textFile('file:///usr/local/spark-1.1.1-bin-hadoop2.4/README.md')
    ```

11. Apply the count action to count the number of lines

    ```python
    textFile.count()
    ```

12. Apply a transformation that only returns lines containing "Spark"

    ```python
    textFile.filter(lambda line: "Spark" in line)
    ```

13. Chain the transformation and action

    ```python
    textFile.filter(lambda line: "Spark" in line).count() # How many lines contain "Spark"?
    ```



13. See http://spark.apache.org/docs/latest/quick-start.html
http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/


Requirements
------------

The following software is needed to get the software from github and run
Vagrant. The Git environment also provides an [SSH client][7] for Windows.

* [Oracle VM VirtualBox][8]
* [Vagrant][9]
* [Git][10]

[7]: http://en.wikipedia.org/wiki/Secure_Shell
[8]: https://www.virtualbox.org/
[9]: http://vagrantup.com/
[10]: http://git-scm.com/

