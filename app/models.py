#app/models.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from sqlalchemy import Column,Integer,String
from app.database import Base

class Estimates(Base):
	__tablename__ = 'Estimates'
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
	hhFarmSizeDisaggregation = Column(String)
	subpopulation = Column(String)
	currencyConversion = Column(String)
	indicatorLevel = Column(String)
	weight = Column(String)
	crosswave = Column(String)
	variableName = Column(String)
	mean = Column(String)
	se = Column(String)
	sd = Column(String)
	p25 = Column(String)
	median = Column(String)
	p75 = Column(String)
	minim = Column(String)
	maxim = Column(String)
	n = Column(String)
	n30 = Column(String)

	def __repr__(self):
		return '<Indicator(Indicator Name=%s, Country=%s, Survey=%s, VarName=%s)>' % (self.indicatorName, self.geography, self.survey, self.variableName)