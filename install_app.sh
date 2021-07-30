#!/bin/bash
. settings.ini
mkdir var 
mkdir var/log
mkdir ldaptrombipy/static/images
sudo apt-get install python3-venv
APP_DIR=$(readlink -e "${0%/*}")

echo $APP_DIR
pip3 install virtualenv
python3 -m virtualenv -p /usr/bin/python3 venv 

source venv/bin/activate
pip install -r requirements.txt

sudo cp trombi.service.template /etc/systemd/system/trombi.service
sudo sed -i "s%{{USER}}%$(whoami)%" /etc/systemd/system/trombi.service

sudo systemctl enable trombi 
sudo systemctl start trombi 