#install and configure nginx
class nginx {

  include puppet::nginx

  package { 'nginx':
    ensure => installed,
    require => Exec['update system'],
  }

  Exec['update system'] {
    command => '/usr/bin/apt-get update',
  }

  nginx::vhost { 'default':
    ensure        => present,
    listen_port   => 80,
    server_name   => ['localhost'],
    www_root      => '/var/www/html',
    index_files   => ['index.html'],
    content => <<EOF
<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
EOF
  }

  nginx::resource { 'redirect':
    location => '/redirect_me',
    rewrite  => {
      source   => '^/redirect_me$',
      destination => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
      permanent => true,
    }
    require => Package['nginx']
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

