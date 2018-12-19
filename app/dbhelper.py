#app/dbhelper.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from app.models import *


def filterFactory(filters, inclusive, model):
	"""
	filterFactory takes a dict of filters and generates a filter for use in
	flask-sqlalchemy queries.
	:param filters: The dict of 
	:param inclusive: boolean value true the factory creates a filter with ands
	:param model: model is the model which is the basis for the filter
	"""
	first = True
	filt = None
	for key,val in filters.items():
		if val and inclusive and not first:
			filt = and_(filt, getattr(model, key).in_(val))
		elif val and filt:
			filt = or_(filt, getattr(model,key).in_(val))
		elif val:
			filt = getattr(model,key).in_(val)
			first = False

	return filt


