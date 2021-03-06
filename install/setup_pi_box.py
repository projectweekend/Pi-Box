import os
import sys
import shutil
import subprocess


if not os.path.exists('/opt/Pi-Box'):
	os.makedirs('/opt/Pi-Box')
shutil.copy('./main.py', '/opt/Pi-Box')

if not os.path.exists('/opt/Pi-Box/dropbox.txt'):
	print('Authorize Pi-Box and obtain the token file: http://raspberry-pi-box.herokuapp.com/')
	print('Copy Dropbox token file (dropbox.txt) to: /opt/Pi-Box.')
	print('Run the installation script again: ./install.sh')
	sys.exit()

print('Example Pi Box path: /home/username/my-pi-box')
pi_box_directory = raw_input('Pi Box path: ')

if not os.path.isdir(pi_box_directory):
	os.makedirs(pi_box_directory)

with open('./install/pi-box-conf-template.txt', 'r') as f:
	upstart_template = f.read()

with open('/etc/init/pi-box.conf', 'w+') as f:
	f.write(upstart_template.format(pi_box_directory))

subprocess.call(['service', 'pi-box', 'restart'])
