# Kills a process name killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  user    => 'root',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
