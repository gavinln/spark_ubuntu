# Commands to run before all others in puppet.
class init {
    group { "puppet":
        ensure => "present",
    }
    case $operatingsystem {
        ubuntu: {
            exec { "apt-update":
                command => "sudo apt-get update",
            }
            Exec["apt-update"] -> Package <| |>
            $misc_packages = ['git-core', 'tmux']
            package { $misc_packages:
                ensure => present,
            }
            package { 'autojump':
                ensure => present,
                require => Exec['apt-update'];
            }
            file { '/etc/profile.d/autojump.sh':
                ensure => present,
                source => '/usr/share/autojump/autojump.sh',
                require => Package['autojump']
            }
        }
    }
}
