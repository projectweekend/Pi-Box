#!/usr/bin/env bash

# Install
apt-get update
apt-get -y upgrade
apt-get -y --force-yes install upstart
pip install -r requirements.txt

# Setup
python ./install/setup_pi_box.py
