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

3. Go to the Spark Docker container directory

    ```bash
    cd /vagrant/docker/spark
    ```

4. Build the Spark image

    ```bash
    sudo docker build --rm -t sequenceiq/spark:1.1.0 .
    ```
5. Run the Spark image

    ```bash
    sudo docker run -i -t sequenceiq/spark /etc/bootstrap.sh -bash
    ```

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

