# This puppet script will create a file in '/tmp/school' containing 'I love puppet'

file { '/tmp/school': #the path of the new file
  ensure  => 'present',
  content => 'I love Puppet', #this text will be inside the file
  owner   => 'www-data',
  group   => 'www-data',
  # mode => '0644',
}
