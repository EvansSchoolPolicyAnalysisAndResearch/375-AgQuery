#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from app import app
from flask import render_template,request

@app.route('/', methods={"GET","POST"})
def index():
	indicators=[]
	if request.form:
		indicators = request.form.getlist("indicatorCategory")
		indicators = indicators + request.form.getlist("geography")
	return render_template("index.html",indicators=indicators)

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/results', methods={"GET","POST"})
def results():
	return render_template("results.html")