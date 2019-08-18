#!/bin/bash
sudo service ntp stop
until ping -nq -c3 8.8.8.8; do
   echo "Waiting for network..."
done
sudo ntpd -gq
sudo service ntp start