#app/dbhelper.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from sqlalchemy.sql import select
from app.models import *



def formHandler(request, session):
	"""
	Handles the input from the filter on the main page.

	This takes in the request information passed to the flask route function
	and turns it into a database query. The results of this query are then
	returned to the original function to either be displayed or transformed
	into a downloadable CSV

	:param request: The request information from the website
	:param sessi
	on: the database session for the query
	:returns: 
	:raises:
	"""
	
	# Pull the information necessary for the db query from the request
	# passed to this function
	geos = request.form.getlist('geography')
	years = request.form.get('years')

	names = request.form.getlist('indicator')

	# If no geographies are selected count them as all selected	
	if not geos :
		geos = session.query(Estimates.geography).distinct()

	if not names:
		return None

	indicators = []	
	
	if years == "most-recent":
		for geo in geos:
			year = getMostRecent(geo, session)
			indicators += session.query(Estimates).filter(
							Estimates.geography == geo, Estimates.year == year,
							Estimates.indicatorName.in_(names)).all()
	else:
		indicators = session.query(Estimates).filter(
			Estimates.geography.in_(geos), 
			Estimates.indicatorName.in_(names)).all()
	return indicators
def getMostRecent(geo, session):
	"""
	Finds the most recent year of LSMS surveys for a given geography

	:param geo: String - the geography you are seeking the most recent year for
	:param session: SQLAlchemy Database session to use for the query
	:returns: String of the most recent survey year for the given geography
	"""

	years = [r.year for r in 
		session.query(Estimates.year).distinct().filter_by(geography= geo)]
	mostRec = "0"
	for yr in years:
		if yr > mostRec:
			mostRec = yr
	return mostRec