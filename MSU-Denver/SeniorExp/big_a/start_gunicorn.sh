#!/bin/bash
source /MSU-Denver/SeniorExp/myprojectenv/bin/activate
cd /Users/chrii/Desktop/MSU-Denver/SeniorExp/big_a
exec gunicorn --workers 3 --bind 0.0.0.0:8000 your_project_name.wsgi:application

