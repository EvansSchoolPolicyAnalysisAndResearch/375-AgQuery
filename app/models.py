#app/models.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from sqlalchemy import Column,Integer,String,Float
from app.database import Base

class Estimates(Base):
	__tablename__ = 'estimates'
	id = Column(Integer, primary_key=True)
	geography = Column(String)
	survey = Column(String)
	instrument = Column(String)
	year = Column(String)
	indicatorCategory = Column(String)
	indicatorName = Column(String)
	units = Column(String)
	cropDisaggregation = Column(String)
	genderDisaggregation = Column(String)
	farmSizeDisaggregation = Column(String)
	subpopulation = Column(String)
	currencyConversion = Column(String)
	indicatorLevel = Column(String)
	weight = Column(String)
	crosswave = Column(String)
	variableName = Column(String)
	mean = Column(Float)
	se = Column(Float)
	sd = Column(Float)
	p25 = Column(Float)
	median = Column(Float)
	p75 = Column(Float)
	minim = Column(Float)
	maxim = Column(Float)
	n = Column(Float)
	nover30 = Column(String)

	def __repr__(self):
		return '"' + '","'.join([self.geography, self.survey, self.instrument,
			self.year, self.variableName]) + '"'

class GenCons(Base):
	__tablename__ = 'gencons'
	topic = Column(String, primary_key=True)
	decision = Column(String)

	def __repr__(self):
		return "<Topic: %s>" % (self.topic)