# Custom nginx header with puppet

# server updating
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# actual installation 
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# the custom response (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# test by startingtart service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
