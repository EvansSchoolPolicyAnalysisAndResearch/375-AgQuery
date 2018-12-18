#app/views.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from app import app
from sqlalchemy.sql import select
from sqlalchemy import and_, or_
from flask import render_template, request, Response
import ast
from app.database import db_session
from app.models import Estimates

@app.route('/', methods={"GET","POST"})
def index():
	"""
	"""
	indicators=[]
	yrs = []
	geos = []

	geography = [r.geography for r in 
		db_session.query(Estimates.geography).distinct()]
	indicatorCategory = [r.indicatorCategory for r in
			db_session.query(Estimates.indicatorCategory).distinct()]
	years = [r.year for r in 
			db_session.query(Estimates.year).distinct()]

	goDisabled = True
	if request.form:
		cats = request.form.getlist('indicatorCategory')
		geos = request.form.getlist('geography')
		yrs = request.form.getlist('years')
		filt = Estimates.indicatorCategory.in_(cats)
		if geos:
			filt = and_(filt, Estimates.geography.in_(geos))
		if yrs:
			filt = and_(filt, Estimates.year.in_(yrs))
		if cats:
			indicators = [r.indicatorName for r in
				db_session.query(Estimates.indicatorName).distinct().filter(filt)]
			if len(indicators) > 0:
				goDisabled = False
	
	return render_template("index.html",indicators=indicators, 
		geography=geography, indicatorCategory=indicatorCategory, 
		goDisabled=goDisabled, years=years,yrs=yrs, geos=geos)

@app.route('/login')
def login():
	"""
	"""
	return render_template("login.html")

@app.route('/results', methods={"POST"})
def results():
	"""
	"""
	indicators = []
	if request.method == "POST":
		geos = ast.literal_eval(request.form.get('geography'))
		yrs = ast.literal_eval(request.form.get('years'))
		indicatorNames = request.values.to_dict()
		# Remove years and geography from the dict of request.values
		del indicatorNames ['years']
		del indicatorNames ['geography'] 
		filt = Estimates.indicatorName.in_(indicatorNames)

		if geos:
			filt = and_(filt, Estimates.geography.in_(geos))
		if yrs:
			filt = and_(filt, Estimates.year.in_(yrs))
		indicators = db_session.query(Estimates).filter(filt)
		headers = Estimates.__table__.columns.keys()
		csvRows =[','.join(headers),]
		csvRows[0] = csvRows[0][3:]
		for ind in indicators:
			csvRows.append(str(ind))

		csv = "\n".join(csvRows)
	return render_template("results.html", indicators=indicators, csv=csv)

@app.route('/get-csv',methods={"POST"})
def get_csv():
		return Response(request.form.get('csv'), mimetype="text/plain",
			headers={
				"Content-Disposition": "attachment;filename=estimates.csv"})

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()