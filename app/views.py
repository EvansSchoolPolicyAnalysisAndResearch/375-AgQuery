#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login')
def index():
	return render_template("login.html")