#!/bin/bash

# Source for this installation script
# https://ranous.files.wordpress.com/2016/03/rtl-sdr4linux_quickstartv10-16.pdf

#Update apt-get
$(sudo apt-get update)

#Install Dependancies
$(sudo apt-get install git)
$(sudo apt-get install cmake)
$(sudo apt-get install build-essential)

#Install C Library
$(sudo apt-get install libusb-1.0-0-dev)

#Build & Compile Drivers
$(git clone git://git.osmocom.org/rtl-sdr.git)
$(cd rtl-sdr/)
$(mkdir build)
$(cd build)
$(cmake ../ -DINSTALL_UDEV_RULES=ON)
$(make)
$(sudo make install)
$(sudo ldconfig)
$(sudo cp ../rtl-sdr.rules /etc/udev/rules.d/)

#Create Driver Blacklist
$(sudo echo "blacklist dvb_usb_rtl28xxu" > blacklist-rtl.conf )

#DO IT
$(echo "Restart to finish installation")
