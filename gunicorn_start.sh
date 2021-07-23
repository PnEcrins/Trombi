#!/bin/bash

APP_DIR=$(readlink -e "${0%/*}")

echo "$APP_DIR"
echo $APP_DIR
. $APP_DIR/settings.ini


cd $APP_DIR
# activate the virtualenv
source $APP_DIR/venv/bin/activate

# Start your gunicorn
exec gunicorn  ldaptrombipy.wsgi:app --error-log $APP_DIR/var/log/trombi_errors.log --pid="${app_name}.pid" --timeout=$gun_timeout -w "${gun_num_workers}"  -b "${gun_host}:${gun_port}"  -n "${app_name}"

