#!/usr/bin/env bash

# Install
apt-get update
apt-get -y upgrade
apt-get -y --force-yes install upstart
pip install -r requirements.txt

# Upstart
cp ./install/pi-box.conf /etc/init

# Move program
mkdir /opt/Pi-Box
cp ./main.py /opt/Pi-Box

# Clean up
rm -r /home/pi/Pi-Box
mkdir /home/pi/Pi-Box
