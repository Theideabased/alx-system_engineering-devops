# This script will install flask from pip3 with version 2.1.0
package{'flask': # The package to install
  ensure   => '2.1.0',
  provider => pip3
}
