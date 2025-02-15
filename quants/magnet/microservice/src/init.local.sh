#!/bin/bash

#chmod +x init.local.sh
#sudo ./init.local.sh
python -m venv python_environment
virtualenv python_environment
source python_environment/bin/activate
pip freeze > requirements.txt
pip list
pip install -r ./requirements.txt
pip list
python3 -m django --version

python3 manage.py runserver
#python3 manage.py startapp auth_app

#docker build -t auth-service .
#docker run -p 8000:8000 auth-service
