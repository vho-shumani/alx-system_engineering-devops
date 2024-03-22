#install flask from pip3.

class { 'python': }

package { 'flask':
  ensure          => installed,
  provider        => 'pip3',
  require         => Class['python'],
  install_options => [ { '--version' => '2.1.0' } ],
}
