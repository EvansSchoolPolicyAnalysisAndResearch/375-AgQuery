#app/models.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Estimates(Base):
	"""
		GenCons extends Base

        Estimates is a class which extends this app's Base, an instance of a 
        SQLAlchemy declarative database. This is the SQLAlchemy representation
        of the estimates table in this project's database. 

	"""
	__tablename__ = 'estimates'
	id = Column(Integer, primary_key=True)
	geography = Column(String)
	survey = Column(String)
	instrument = Column(String)
	year = Column(String)
	indicatorCategory = Column(String)
	indicator = Column(String)
	units = Column(String)
	cropDisaggregation = Column(String)
	genderDisaggregation = Column(String)
	farmSizeDisaggregation = Column(String)
	ruralortotal = Column(String)
	subpopulation = Column(String)
	currencyConversion = Column(String)
	indicatorLevel = Column(String)
	weight = Column(String)
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
		return "<Variable Name: %s; Instrument: %s>" % \
			(self.variableName, self.instrument)

class IndCons(Base):
	""" 
		IndCons extends Base

        Indcons is a class which extends this app's Base, an instance of a 
        SQLAlchemy declarative database. This is the SQLAlchemy representation
        of the indcons table in this project's database. 

	"""
	__tablename__ = 'indcons'
	indicatorCategory = Column(String)
	indicator = Column(String)
	varnamestem = Column(String, primary_key=True)
	genderDisaggregation = Column(String)
	farmSizeDisaggregation = Column(String)
	cropDisaggregation = Column(String)
	subpopulation = Column(String)
	rowsperinstrument = Column(String)
	numerator = Column(String)
	denominator = Column(String)
	units = Column(String)
	indicatorLevel = Column(String)
	weight = Column(String)
	constructiondecision = Column(String)
	winsorizing = Column(String)

	def __repr__(self):
		return "<Indicator Name: %s; Construction Decision: %s>" % \
			(self.indicator, self.constructiondecision)

class CntryCons(Base):
	"""
		CntryCons extends Base
	
		CntryCons is a class which extends this app's Base class, a SQLAlchemy
		declarative database. This class represents the cntrycons table in the
		project's database. 
	
	"""
	__tablename__ = "cntrycons"
	id = Column(Integer, primary_key=True)
	instrument = Column(String)
	cntrydec = Column(String)
	indicator = Column(String, ForeignKey(IndCons.indicator))

	indcon = relationship('IndCons', foreign_keys = 'CntryCons.indicator', lazy="joined")

	def __repr__(self):
		return "<Instrument: %s; IndCon ID: %s>" % \
			(self.instrument, self.indid)