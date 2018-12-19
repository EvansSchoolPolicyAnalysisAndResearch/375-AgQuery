#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from app import app
from sqlalchemy.sql import select
from sqlalchemy import and_, or_
from flask import render_template, request, Response
import ast
from app.database import db_session
from app.models import Estimates
from app.dbhelper import filterFactory

@app.route('/', methods={"GET","POST"})
def index():
	"""
	"""

	# Creating the variables to be used throughout the method
	indicators=[] # the list of indicators to display
	filterDict = {} # dict of attributes and lists for building a filter
	goDisabled = True # Is the go button on the page disabled

	# These database queries are for populating the filter lists at the top of
	# the page
	geography = [r.geography for r in 
		db_session.query(Estimates.geography).distinct()]
	indicatorCategory = [r.indicatorCategory for r in
			db_session.query(Estimates.indicatorCategory).distinct()]
	years = [r.year for r in 
			db_session.query(Estimates.year).distinct()]

	# If this page was accessed using post then request.form should not be 
	# empty. In which case this code block will get the list of indicator names
	# to be displayed in the indicators filter.
	if request.form:
		# Pull the information necessary from the post information

		# The only absolutely necessary filter is the indicator category. The
		# rest default to all.
		selectedCategories = request.form.getlist('indicatorCategory')
		if selectedCategories:
			indicators = [r.indicatorName for r in
				db_session.query(
					Estimates.indicatorName).distinct().filter(
						Estimates.indicatorCategory.in_(selectedCategories))]
			# If the db query returned something, enable the go button
			if len(indicators) > 0:
				goDisabled = False
	
	return render_template("index.html",indicators=indicators, 
		geography=geography, indicatorCategory=indicatorCategory, 
		goDisabled=goDisabled, years=years)

@app.route('/login')
def login():
	"""
	"""
	return render_template("login.html")

@app.route('/results', methods={"POST"})
def results():
	"""
	"""
	indicators = []
	filterDict = {}
	if request.method == "POST":
		# Pull the information necessary for the db query from the post
		# information
		filterDict['geography'] = request.form.getlist('geography')
		filterDict['year'] = request.form.getlist('years')
		filterDict['indicatorName'] = request.values.to_dict()
		
		# Request.values.to_dict() also gives the values for year and geos,
		# Those need to be removed from the dict of indicator names
		
		del filterDict['indicatorName'] ['years']
		del filterDict['indicatorName'] ['geography']


		# Query the database to get the estimates.
		indicators = db_session.query(Estimates).filter(filterFactory(filterDict, True, Estimates))

		# Building the rows of the CSV
		# This is horrible code that should be replaced before the final
		# version as it relies on the order of the keys in the code.
		headers = Estimates.__table__.columns.keys()
		csvRows =[','.join(headers),]
		csvRows[0] = csvRows[0][3:]
		for ind in indicators:
			csvRows.append(str(ind))
		# Combine all of the rows into a single row.
		csv = "\n".join(csvRows)
	return render_template("results.html", indicators=indicators, csv=csv)

@app.route('/get-csv',methods={"POST"})
def get_csv():
		return Response(request.form.get('csv'), mimetype="text/plain",
			headers={
				"Content-Disposition": "attachment;filename=estimates.csv"})

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()