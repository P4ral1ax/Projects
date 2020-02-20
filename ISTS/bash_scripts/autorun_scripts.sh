#! /bin/bash

echo 'Make sure program was run with SUDO privelages'
echo 'Auto Running Script Package'

echo 'Password Change Quickrun.....'
$(sudo python3 ../pass_change/pass_change.py)
echo '1'

echo 'Set Firewall....'
#$(sudo python3 firewall_default.py)

echo 'SSH Secure....'
#$(sudo python3 ssh_secure.py)

echo 'Secure Settings....'
#$(sudo python3 default_settings.py)

echo 'file_mon with default.....'
$(sudo python3 ../file-mon/file-mon.py)
echo '1'

echo 'Raw Detect.....'
#$(sudo python3 raw_detect.py)

echo 'Get Security Software......'
#$(apt-get ...)
#$(apt-get install ...)
