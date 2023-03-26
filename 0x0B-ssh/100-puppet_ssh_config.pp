# Changes SSH config file
file { '/home/user/.ssh/config':
  ensure => present,
  owner  => 'user',
  group  => 'user',
  mode   => '0600',
  content => "Host server\n\tHostName server.example.com\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n"
}
