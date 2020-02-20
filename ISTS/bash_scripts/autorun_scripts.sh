#! /bin/bash

echo 'Make sure program was run with SUDO privelages'
echo 'Auto Running Script Package'

echo 'Password Change Quickrun.....'
$(sudo python3 ../pass_change/pass_change.py)
echo '1'

echo 'file_mon with default.....'
$(sudo python3 ../file-mon/file-mon.py)
echo '1'

echo 'Secure Settings....'
#$(sudo python3 default_settings.py)

echo 'SSH Secure....'
#$(sudo python3 .ssh_secure.py)

echo 'Raw Detect.....'
#$(sudo python3 raw_detect.py)

echo 'Set Firewall....'
#$(sudo python3 firewall_default.py)
