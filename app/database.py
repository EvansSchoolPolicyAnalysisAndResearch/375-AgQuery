#app/models.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Estimates(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	geography = db.Column(db.String)
	survey = db.Column(db.String)
	instrument = db.Column(db.String)
	year = db.Column(db.String)
	indicatorCategory = db.Column(db.String)
	indicatorName = db.Column(db.String)
	units = db.Column(db.String)
	cropDisaggregation = db.Column(db.String)
	genderDisaggregation = db.Column(db.String)
	hhFarmSizeDisaggregation = db.Column(db.String)
	subpopulation = db.Column(db.String)
	currencyConversion = db.Column(db.String)
	indicatorLevel = db.Column(db.String)
	weight = db.Column(db.String)
	crosswave = db.Column(db.String)
	variableName = db.Column(db.String)
	mean = db.Column(db.String)
	se = db.Column(db.String)
	sd = db.Column(db.String)
	p25 = db.Column(db.String)
	median = db.Column(db.String)
	p75 = db.Column(db.String)
	minim = db.Column(db.String)
	maxim = db.Column(db.String)
	n = db.Column(db.String)
	n30 = db.Column(db.String)

	def __repr__(self):
		return '<Indicator(Indicator Name=%s, Country=%s, Survey=%s, VarName=%s)>' % (self.indicatorName, self.geography, self.survey, self.variableName)