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


def filterFactory(filters, inclusive, model):
	"""
	A very simple factory for building very simple filters. 

	filterFactory takes a dict of filters and creates a compound IN SQL query 
	using SQLALchemy's and_(), or_(), and in_() functions. An example SQL query buildable with this factory would be: 
		WHERE key1 IN vals1 AND key2 IN vals2 AND key3 IN vals3


	:param filters: The dict of filter values. Keys must be the same as the 
	name of database Column rows. The values in the dict should be lists of 
	values.
	:param inclusive: Boolean True - filter is built out of ands; False - 
	filter is built out of ors
	:param model: Is the SQLAlchemy ORM which is being queried
	:returns: SQLAlchemy BinaryExpression object which can be passed to a sqlalchemy filter() call.
	:raises AttributeError: raises an exception if a key in filters is not an
	attribute of model
	"""

	filtCreated = False
	filt = None

	# This loop is where the action is
	for key,val in filters.items():
		if val and inclusive and  filtCreated:
			filt = and_(filt, getattr(model, key).in_(val))
		elif val and filtCreated:
			filt = or_(filt, getattr(model,key).in_(val))
		elif val:
			filt = getattr(model,key).in_(val)
			filtCreated = True

	return filt

def formHandler(request, session):
	"""
	Handles the input from the filter on the main page.

	This takes in the request information passed to the flask route function
	and turns it into a database query. The results of this query are then
	returned to the original function to either be displayed or transformed
	into a downloadable CSV

	:param request: The request information from the website
	:param session: the database session for the query
	:returns: 
	:raises:
	"""
	
	# Set the scope for the indicators variable
	filtCreated = False
	filt = None
	filterDict= {}
	
	# Pull the information necessary for the db query from the request
	# passed to this function
	filterDict['geography'] = request.form.getlist('geography')
	years = request.form.get('years')
	filterDict['indicatorName'] = request.values.to_dict()
	
	# Request.values.to_dict() also gives the values for year and geos,
	# Those need to be removed from the dict of indicator names	
	del filterDict['indicatorName'] ['years']
	if filterDict['geography']:
		del filterDict['indicatorName'] ['geography']
	else:
		filterDict['geography'] = [r.geography for r in 
			session.query(Estimates.geography).distinct()]


	# Build the filter for the query.
	if years == "Most Recent Survey":
		for geo in filterDict['geography']:
			# Get the most recent year for each country
			mry = getMostRecent(geo, session)

			# Test to see if the filt already exists.
			if not filtCreated:
				# Add this country/year combo to the filter
				filt = or_(filt, 
					and_(Estimates.geography.is_(geo), 
						Estimates.year.is_(mry)))
			else:
				# Filter is new, create the first entry
				filt = and_(Estimates.geography.is_(geo),
						Estimates.year.is_(mry))
				filtCreated=True
		# Add the requested indicators to the filter
		filt = and_(filt, Estimates.indicatorName.in_(filterDict['indicatorName']))	
	else:
		# If all years is selected, use the filterFactory function
		filt = filterFactory(filterDict, True, Estimates)
	
	# Query the database to get the estimates and return the results
	return session.query(Estimates).filter(filt)

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