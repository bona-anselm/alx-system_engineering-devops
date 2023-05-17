# A script that increase the limit of cuncurrent tasks
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2048'\n",
}
sudo service nginx restart
