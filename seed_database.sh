#!/bin/bash

rm db.sqlite3
rm -rf ./daytripperapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations daytripperapi
python3 manage.py migrate daytripperapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata item_types
python3 manage.py loaddata activity_types
python3 manage.py loaddata transportation_types
python3 manage.py loaddata planners
python3 manage.py loaddata trips
python3 manage.py loaddata packitems
python3 manage.py loaddata activities

