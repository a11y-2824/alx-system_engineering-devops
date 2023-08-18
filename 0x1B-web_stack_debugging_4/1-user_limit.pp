# This manifest will change the OS configuration 
# Allow login with the holberton user
# open a file without any error message
exec {'new-login':
  provider => 'shell',
  command  => 'sudo adduser --disabled-password',
}

