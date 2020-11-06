#!python3

#data/db_updater.py

"""

"""

__copyright__ = """
Copyright 2019 Evans Policy Analysis and Research Group (EPAR).
"""

__license__ = """
This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

import argparse
import csv
import os
import shutil
import subprocess
import sys
import urllib.request
import xlrd

# Download the file from `url` and save it locally under `file_name`:


INDCOLUMN 		= 1
INSTRUMENTS 	= ("ETH ESS Wave 1", "ETH ESS Wave 2", "ETH ESS Wave 3", "NGA GHSP Wave 1", "NGA GHSP Wave 2", "NGA GHSP Wave 3", "TZA NPS Wave 1", "TZA NPS Wave 2", "TZA NPS Wave 3", "TZA NPS Wave 4")
INDICATORCOL	= 6
CROPCOL			= 8
CLEAN_EST 		= 'estimates_cleaned.csv'
CLEAN_DECS		= 'decs_cleaned.csv'
CLEAN_CTRY_DECS	= 'ctry_decs_cleaned.csv'
EST_CSV			= 'estimates.csv'
DECS_CSV		= 'decs.csv'
EXCEL_WORKBOOK	= 'indicator-workbook.xlsx'
EXCEL_URL		= 'https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination/raw/master/EPAR_UW_335_AgDev_Indicator_Estimates.xlsx'

hexmatcher = {}
################################################################################
#                                 CSV HANDLING                                 #
################################################################################

def read_csv(infile):
	"""
	Reads a CSV File into memory as a list of lists. Each inner list represents
	one row of the CSV.

	:param infile	: an open file to be read into memory
	:returns		: A list of lists containing the contents of the csv file
	"""
	rows = []
	rdr = csv.reader(infile, delimiter=',', quotechar='"', 
		quoting=csv.QUOTE_NONNUMERIC)
	for row in rdr:
		rows.append(row)
	return rows


def write_csv(rows, filename):
	"""
	Writes  a CSV stored as a list of lists from memory to disk
	
	:param rows		: a list of csv rows (lists) to be written
	:param outfile	: an open file for writing
	"""
	with open(filename, 'w') as outfile:
		wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
					quoting=csv.QUOTE_NONNUMERIC)
		wrtr.writerows(rows)

def sheet_to_csv(sheet, filename):
	"""
	Writes  an Excel Sheet into a CSV on disk
	
	:param sheet	: an xlrd sheet oo be written to disk
	:param filename	: an open file for writing
	"""
	write_csv(sheet_to_list(sheet), filename)

################################################################################
#                                EXCEL HANDLING                                #
################################################################################

def extract_sheets(excel_file):
	"""
	Extracts the estimates and construction decision sheets from the EPAR 335
	AgDev indicator estimates spreadsheet

	:param excel_file	: an opened excel file to be read 
	:returns			: a tuple containing the two sheets from the file
	"""
	workbook = xlrd.open_workbook(excel_file, on_demand = True)
	sheets = workbook.sheet_names()
	est_name = [sheet for sheet in sheets if "Estimates" in sheet]
	con_name = [sheet for sheet in sheets if "Indicator Construction" in sheet]
	estimates = None
	construction = None
	if len(est_name) == 1:
		estimates = workbook.sheet_by_name(est_name[0])
	else:
		print("Could not find estimates sheet, assuming second sheet by index")
		estimates = workbook.sheet_by_index(1)

	if len(con_name) == 1:
		construction = workbook.sheet_by_name(con_name[0])
	else:
		print("Could not find construction sheet, assuming third sheet by index")
		construction = workbook.sheet_by_index(2)

	return (estimates, construction)



def sheet_to_list(sheet):
	"""
	converts an Excel sheet into a list of lists
	
	:param sheet	: an xlrd sheet oo be written to disk
	:returns		: an open file for writing
	"""
	c = []
	for i in range(sheet.nrows):
		c.append([])
		for j in range(sheet.ncols):
			if sheet.cell_type(i, j) == xlrd.sheet.XL_CELL_EMPTY:
				c[i].append(0)
			else:
				c[i].append(sheet.cell_value(i, j))

	return c

################################################################################
#                                DATA  CLEANING                                #
################################################################################

def clean_estimates(rows):
	"""
	Cleans rows of the estimates csv into format used by the indicator query
	tool 

	:param rows	: a list of csv rows (lists) to be cleaned 
	:returns	: the cleaned version of the list
	"""
	output = []

	# Get rid of the headers
	rows.pop(0)
	for r,row in enumerate(rows):
		# Add the ID to the row
		row.insert(0, r)
		# Clean the elements of the row
		for i in range(len(row)) :
			if row[i] == "0 ":
				row[i] = 0
			elif row[i] == "1": 
				row[i] = 1
			elif type(row[i]) == str:
				row[i] = row[i].strip()

		if ' - large ruminants, small ruminants, poultry' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - large ruminants, small ruminants, poultry', '')
			row[CROPCOL] = "All livestock"
		elif ' - large ruminants' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - large ruminants', '')
			row[CROPCOL] = "Large ruminants"
		elif ' - small ruminants' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - small ruminants', '')
			row[CROPCOL] = "Small ruminants"
		elif ' - poultry' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - poultry', '')
			row[CROPCOL] = "Poultry"
		elif ' - cows' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - cows', '')
			row[CROPCOL] = "Cows"
		elif ' - buffalos' in row[INDICATORCOL]:
			row[INDICATORCOL] = row[INDICATORCOL].replace(' - buffalos', '')
			row[CROPCOL]="Buffalos"
		elif row[INDICATORCOL] == "Milk productivity":
			row[CROPCOL] = "Large ruminants"
		if  row[INDICATORCOL] in hexmatcher:
			row.insert(1, hexmatcher[row[INDICATORCOL]])
		else:
			print(row[INDICATORCOL])
			row.insert(1, 'NA')
		output.append(row)
	return output


def clean_decisions(rows):
	"""
	Cleans rows of a indicator construction decision csv into format used by 
	the indicator query tool 

	:param rows	: a list of csv rows (lists) to be cleaned 
	:returns	: the cleaned version of the list
	"""
	indcons = []
	cntrycons = []
	def make_id_counter():
		""" 
		Simple little closure for getting the next available id number
		
		:returns	: a function which will produce the next number in sequence
		"""
		next_id = 1
		def id_counter():
			nonlocal next_id
			id_num = next_id
			next_id += 1
			return id_num
		
		return id_counter

	def make_hex_counter():
		id_ctr = make_id_counter()
		def hex_counter():
			nonlocal id_ctr
			return hex(id_ctr())[2:]
		return hex_counter


	get_id = make_id_counter()
	# Get rid of the headers
	rows.pop(0)
	get_hex = make_hex_counter()

	for r,row in enumerate(rows):
		# Row Stub is the the elements needed for the non-country
		# specific information
		row_stub = row[0:15]
		# Clean the data up a bit, removig excess spaces, making
		# sure numbers are viewed as numbers not strings, etc.
		for i,elem in enumerate(row_stub) :
			if elem == "0 ":
				row_stub[i] = 0
			elif elem == "1": 
				row_stub[i] = 1
			elif type(elem) == str:
				row_stub[i] = elem.strip()
			else:
				row_stub[i] = elem
		# Add a unique ID to the 
		row_stub.insert(0, get_hex())
		hexmatcher[row_stub[INDCOLUMN]]= row_stub[0]
		indcons.append(row_stub)
		for i,inst in enumerate(INSTRUMENTS):
			 cntrycons.append([get_id(), inst, row[i+15], row_stub[INDCOLUMN]])
	return (indcons, cntrycons)




def excel_extraction(filename):
	estimates, construction = extract_sheets(filename)
	sheet_to_csv(estimates, 'estimates.csv')
	sheet_to_csv(construction, 'construction.csv')

def construction_cleaning(file):
	# Clean the file
	indcons, cntrycons = clean_decisions(read_csv(file))
	# Write the output to files
	write_decisions(indcons, CLEAN_DECS)
	write_decisions(cntrycons, 'construction_countries_cleaned.csv')

def estimates_cleaning(file):
	write_csv(clean_estimates(read_csv(file)), CLEAN_EST)


def downloader(url, filename):
	
	with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)

def full_update():
	# Download the spreadsheet
	downloader(EXCEL_URL, EXCEL_WORKBOOK)
	# Extract the relevant sheets from the workbook
	estimates, decisions = extract_sheets(EXCEL_WORKBOOK)
	# Clean the data
	decs_clean, ctry_decs = clean_decisions(sheet_to_list(decisions))
	est_clean = clean_estimates(sheet_to_list(estimates))
	# Save to CSVs
	write_csv(est_clean, CLEAN_EST)
	write_csv(decs_clean, CLEAN_DECS)
	write_csv(ctry_decs, CLEAN_CTRY_DECS)

	# Run the sql query
	print("Using username: " + os.getenv('PSQL_USERNAME', '\'epardata\' (default)'))
	subprocess.run(['psql', f"--username={os.getenv('PSQL_USERNAME', 'epardata')}", '--dbname=epardata', 
		'--file=update-database.sql'])

if __name__ == "__main__":
	pars = argparse.ArgumentParser(description = __doc__, 
		epilog = __copyright__ + __license__,
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	pars.add_argument( '-x', '--extract-sheets',
		dest	= 'excel',
		metavar	= 'EXCEL_WB',
		help	= "path for the input excel file")
	pars.add_argument( '-c', '--clean-decs',
		metavar	= 'DECISION_CSV',
		dest	= 'decs',
		type 	= argparse.FileType('r'),
		help	= "path for the input consruction decision csv file")
	pars.add_argument( '-e', '--clean-estimates',
		metavar	= 'EST_CSV',
		dest	= 'ests',
		type 	= argparse.FileType('r'),
		help	= "path for the input estimates csv file")
	# Parse passed arguments
	args = pars.parse_args()

	if len(sys.argv) == 1:
		full_update()
	if args.excel:
		excel_extraction(args.excel)
	if args.decs:
		construction_cleaning(args.decs)
	if args.ests:
		estimate_cleaning(args.ests)

