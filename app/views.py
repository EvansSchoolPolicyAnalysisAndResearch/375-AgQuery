#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from app import app
from sqlalchemy.sql import select
from flask import render_template,request
from app.database import db_session
from app.models import Estimates

@app.route('/', methods={"GET","POST"})
def index():
	"""
	"""
	indicators=[]
	geography = [r.geography for r in 
		db_session.query(Estimates.geography).distinct()]
	indicatorCategory = [r.indicatorCategory for r in
			db_session.query(Estimates.indicatorCategory).distinct()]
	goDisabled = True
	if request.form:
		cats = request.form.getlist('indicatorCategory')
		geos = request.form.getlist('geography')
		if cats and geos:
			goDisabled = False
			indicators = [r.indicatorName for r in
				db_session.query(Estimates.indicatorName).distinct().filter(Estimates.indicatorCategory.in_(cats),
					Estimates.geography.in_(geos))]
	
	return render_template("index.html",indicators=indicators, geography=geography, indicatorCategory=indicatorCategory, goDisabled=goDisabled)

@app.route('/login')
def login():
	"""
	"""
	return render_template("login.html")

@app.route('/results', methods={"GET","POST"})
def results():
	"""
	"""
	if request.method == "POST":
		indicatorNames = request.values
		indicators = db_session.query(
			Estimates).filter(
				Estimates.indicatorName.in_(indicatorNames))

		for ind in indicators:
			pass
	return render_template("results.html", indicators=indicators)

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()