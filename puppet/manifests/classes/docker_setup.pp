# Setup docker and download & run images
class docker_setup {
    class { 'docker':
        tcp_bind    => 'tcp://0.0.0.0:2375',
        socket_bind => 'unix:///var/run/docker.sock';
    }
    user {'vagrant':
        ensure => 'present'
    }
    exec {"vagrant_in_docker":
      unless => "grep -q 'docker\\S*vagrant' /etc/group",
      command => "usermod -aG docker vagrant",
      require => [User['vagrant'], Class['docker']]
    }
    docker::image { 'sequenceiq/hadoop-docker:2.6.0':
        ensure    => 'present',
        require => Class[docker]
    }
    # ::docker::run { 'rabbitmq:3-management':
    #     image   => 'rabbitmq:3-management',
    #     tty     => true,
    #     ports   => ['15672:15672', '5672:5672'],
    #     require => Docker::Image['rabbitmq:3-management'],
    # }
}

