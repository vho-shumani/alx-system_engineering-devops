ass for Nginx configuration
class nginx {

  # Include the Nginx module (assuming it's installed and configured)
  include puppet::nginx

  # Package resource to install Nginx
  package { 'nginx':
    ensure => installed,
    require => Exec['update system'],
  }

  # Update package lists
  Exec['update system'] {
    command => '/usr/bin/apt-get update',
  }

  # Default server configuration
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

  # Redirect configuration for /redirect_me (using Nginx module)
  nginx::resource { 'redirect':
    location => '/redirect_me',
    rewrite  => {
      source   => '^/redirect_me$',
      destination => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
      permanent => true,
    }
    require => Package['nginx']
  }

  # Service resource to manage Nginx
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

