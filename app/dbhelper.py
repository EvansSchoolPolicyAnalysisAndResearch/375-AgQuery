#app/dbhelper.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from app.models import *
from flask_sqlalchemy import SQLAlchemy
from flask import Markup

from sqlalchemy import and_, or_
from sqlalchemy.sql import select

from markdown import markdown
from collections import OrderedDict

def formHandler(request, session):
	"""
	Handles the input from the filter on the main page.

	This takes in the request information passed to the flask route function
	and turns it into a database query. The results of this query are then
	returned to the original function to either be displayed or transformed
	into a downloadable CSV.

	:param request: The request information from the website
	:param session: the database session for the query
	:returns: 		Results of the Database Query or None for no results
	"""
	
	# Pull the information necessary for the db query from the request
	# passed to this function
	geoyears = request.values.getlist('geo_year')
	inds = request.values.getlist('indicator')
	
	# Check to make sure the user is not attempting sql injection or submitting
	# invalid database entries.
	if not validateRequest(session, inds, geoyears):
		return None

	indicators = []	
	# Loop through the geography/year options and get the estimates and
	# decisions from the database
	for gy in geoyears:
		# Split the geoyear into two pieces - geography and year
		geo,year = gy.split("_", 1)
		# Query the database
		indicators += session.query(Estimates, CntryCons).filter(
			Estimates.indicator == CntryCons.indicator,
			Estimates.instrument == CntryCons.instrument).filter(
			Estimates.geography == geo, 
			Estimates.year == year,
			Estimates.hexid.in_(inds)).all()
	return indicators


def validateRequest(session, indicators, geoyears, commodity = None):
	"""
	
	:param dbsession:	A db session for obtaining valid responses
	:param indicators:	The indicators
	:param geoyears:	The geoyears
	:param commodity:	The commodity
	
	:returns:  			The 
	"""
	# Get the list of valid indicator hex ids and geoyear combinations from the
	# database.
	validinds = [r.hexid for r in session.query(IndCons.hexid).all()]
	validgeoyears = [r.geography + "_" + r.year for r in session.query(Estimates.geography, Estimates.year).distinct()]

	# Test if the requested indicators are valid
	if not set(indicators).issubset(set(validinds)):
		return False
	# Test if the geoyear combos are valid
	if not set(geoyears).issubset(set(validgeoyears)):
		return False
	# Nothing showed up as invalid return true
	return True

