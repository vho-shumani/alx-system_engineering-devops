# Install and configure an nginx server
exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
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

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
