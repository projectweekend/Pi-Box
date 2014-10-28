#!/usr/bin/env bash

apt-get update
apt-get -y upgrade
apt-get -y --force-yes install upstart

cp ./install/pi-box.conf /etc/init

pip install -r requirements.txt
