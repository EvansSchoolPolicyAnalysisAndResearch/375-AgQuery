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
from app.database import db_session


def filterFactory(filters, inclusive, model):
	"""
	A very simple factory for building very simple filters. 

	filterFactory takes a dict of filters and creates a compound IN SQL query 
	using SQLALchemy's and_(), or_(), and in_() functions. An example SQL query buildable with this factory would be: 
		WHERE key1 IN val1 AND key2 IN v AND key3 IN val3


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
	first = True
	filt = None

	# This loop is where the action is
	for key,val in filters.items():
		if val and inclusive and not first:
			filt = and_(filt, getattr(model, key).in_(val))
		elif val and filt:
			filt = or_(filt, getattr(model,key).in_(val))
		elif val:
			filt = getattr(model,key).in_(val)
			first = False

	return filt

def mostRecent(model, geography)



def getMostRecent(geo):
	"""
	getMostRecent 
	"""
	years = [r.year for r in 
		db_session.query(Estimates.year).distinct().filter_by(geography= geo)]
	mostRec = "0"
	for yr in years:
		if yr > mostRec:
			mostRec = yr
	return mostRec