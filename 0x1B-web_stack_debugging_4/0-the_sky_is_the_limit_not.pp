# A script that increase the limit of cuncurrent tasks
exec { 'increase_nginx_ulimit':
  command     => "echo 'ULIMIT=\"-n 4096\"' >> /etc/default/nginx",
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}

