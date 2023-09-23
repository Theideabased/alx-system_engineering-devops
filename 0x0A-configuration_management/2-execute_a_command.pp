# This will kill a procrss named killmenow
exec{'killmenow': # The name of process to kill
  command => 'pkill killmenow', # killing the process
  path    => '/usr/bin' # The path where the pkill command is located use 'which pkill to find it'
}
