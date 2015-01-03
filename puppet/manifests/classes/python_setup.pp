# install python
class python_setup {
    case $operatingsystem {
        ubuntu: {
            package { ['build-essential', 'checkinstall', 'python-dev']:
                ensure => present
            }
            package { "python-pip":
                ensure => installed
            }
            package { 'fig':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'flask':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'nose':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
            package { 'yarn-api-client':
                ensure => installed,
                provider => pip,
                require => Package['python-pip']
            }
        }
    }
}
