#!/bin/bash

echo "Setting up "
apt-get install python-pip
sudo pip install virtualenv
echo "installing dependencies"
virtualenv virtual_env --python=/usr/bin/python3.7
source virtual_env/bin/activate
pip3 install flask
pip3 install flask_restful
pip3 install flask_jwt_extended
pip3 install flask_sqlalchemy
pip3 install tika
pip3 install flask_cors
pip3 install pymysql
pip install mysqlclient
pip3 install MySQL-python
echo "finished"
echo "$ source virtual_env/bin/activate to activate the environment"
echo "to run the app enter: $FLASK_APP=app.py flask run"

