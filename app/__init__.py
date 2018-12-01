#app/init.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see
license.txt file for more information.
"""


from flask import Flask

# initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the Config file
app.config.from_object('config')


