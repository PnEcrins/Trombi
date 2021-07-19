#!/bin/bash
APP_DIR=$(readlink -e "${0%/*}")

echo $APP_DIR
python3 -p /usr/bin/python3 -m venv 

source venv/bin/activate
pip install -r requirements.txt

sudo cp trombi.service.template /etc/systemd/system/trombi.service
sudo sed -i "s%{{USER}}%${USER}%" /etc/systemd/system/trombi.service

sudo systemctl enable trombi 
sudo systemctl start trombi 
