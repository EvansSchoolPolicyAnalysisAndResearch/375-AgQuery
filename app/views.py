#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the
license.txt file for more information.
"""
from app import app
from app.database import db_session
from app.models import *
from app.dbhelper import formHandler
from app.dlhelper import make_csv

from sqlalchemy.sql import select
from flask import render_template, request, Response


@app.route('/', methods={"GET","POST"})
def index():
	"""
	Handles requests to the main page of the website

	This function handles all of the requests to the default page it takes
	no parameters, but relies on the request.form global for the flask
	session to populate the indicators for the selected category

	:returns: HTML file representing the index page
	"""

	# the list of selectable indicators
	indicators = db_session.query(IndCons.indicator, IndCons.hexid).all()
	# sort the list of indicators alphabetically
	indicators.sort(key=lambda i: i.indicator)
	# Get a list of all of the geography/year combos in the db
	db_geo = db_session.query(Estimates.geography, Estimates.year).distinct()
	# Create a dict to store each geo and the years available for that geo
	crops = db_session.query(Estimates.cropDisaggregation).distinct()
	print(db_geo)
	geos = {}
	# place the years into different geographies
	for g in db_geo:
		if g.geography in geos.keys():
			geos[g.geography].append(g.year)
		else:
			geos[g.geography] = [g.year]

	# Sort the lists of years before displaying them
	for g in geos.keys():
		geos[g].sort()
	
	#Get Gender
	genders = db_session.query(Estimates.genderDisaggregation).distinct().order_by(Estimates.genderDisaggregation)

 
	#Get farm Sizes
	farmSizes = db_session.query(Estimates.farmSizeDisaggregation).distinct().order_by(Estimates.farmSizeDisaggregation)


	return render_template("index.html",indicators=indicators,
		geoyears=geos, crops=crops, genders = genders, farmSizes = farmSizes) #???????

	

@app.route('/login')
def login():
	"""
	Place holder for a login page

	This will be where any login handling will be done when the login
	system is created

	:returns: HTML page for displaying a login screen.
	"""
	return render_template("login.html")

@app.route('/results', methods={"GET", "POST"})
def results():
	"""
	Creates the results page

	Passes the filter state from the index page to the form handler function
	before passing the results to the JINJA Template for rendering into an
	HTML page which is returned. Requires the request object to have the
	necessary filters.

	:returns: an HTML page to be displayed by the website
	"""
	# If the user got here without submitting form data reply with no
	# indicator selected page

	indicators = formHandler(request, db_session)
	#sort the indicators alphabetically
	indicators.sort(key=lambda i: i.Estimates.indicator)
	# Check if anything is returned from the formHandler. If no, then show the
	# error page
	if not indicators:
		return render_template("no-inds.html"), 406
	#Grab the GET query containing the filters and pass to results page
	r = str(request)
	filters = r[r.find("?") + 1 : r.find("'", r.find("'") + 1)]
	return render_template("results.html", indicators=indicators, filters=filters)

@app.route('/get-csv',methods={"GET","POST"})
def get_csv():
	"""
	Handles requests to download CSV Files containing the estimates

	Passes the state of the filters on the index page to the formHandler
	function. It then collates the results into a CSV file which is
	then offered as a download by the website.

	:returns: a Response object containing a CSV of the required variables
	"""
	# Get the estimates from the formhandler
	indicators = formHandler(request, db_session)
	#sort the indicators alphabetically
	indicators.sort(key=lambda i: i.Estimates.indicator)
	# Check if any indicators were selected
	if not indicators:
		return render_template("no-inds.html"), 406

	indicators = [r.Estimates for r in indicators]

	# Get the headers based on the columns of the database
	headers = Estimates.__table__.columns.keys()
	headers = headers[1:]

	#Generate a string which is the final csv
	csv = make_csv(headers, indicators)

	return Response(csv, mimetype="text/csv",
			headers={"Content-Disposition":
				"attachment;filename=indicator_estimates.csv"})

@app.route('/about-data/')
def about_data():
	"""
	For our purposes the about_data page is now on our website. Redirect in
	case anyone still has the old link
	"""
	return redirect("https://evans.uw.edu/policy-impact/epar/agricultural-development-data-curation#construction",
		code=301)

@app.teardown_appcontext
def shutdown_session(exception=None):
	"""
	When the http session is over this kills the database session.

	:returns: none
	"""
	db_session.remove()
