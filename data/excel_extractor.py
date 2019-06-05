#!python3

# data/excel_extractor.py

"""

	This script takes the name of an excel file and extracts the data needed for the database. It specifically looks for sheets

"""

__copyright__ = """
Copyright 2019 Evans Policy Analysis and Research Group (EPAR).
"""

__license__ = """
This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
# import argparse - Argparse is only needed if this is called directly.
import csv
import xlrd
import re

def read_excel(excel_file):
	return xlrd.open_workbook(excel_file, on_demand = True)

def extract_data(workbook):
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

def write_csv(file, sheet):
	wrtr = csv.writer(file, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_NONNUMERIC)
	for i in range(sheet.nrows):
		wrtr.writerow(sheet.row_values(i))

if __name__ == "__main__":
	import argparse
	# Set up commandline interface
	pars = argparse.ArgumentParser( description = __doc__,
		epilog 			= __copyright__ + __license__,
		formatter_class	= argparse.ArgumentDefaultsHelpFormatter)
	
	pars.add_argument( 'file', 
		nargs	='?',
		metavar	= 'INPUT',
		default	= 'EPAR_UW_335_AgDev_Indicator_Estimates.xlsx', 
		help	= "path for the input excel file")
	
	pars.add_argument('-d', '--construction', 
		metavar	= 'OUTPUT1', 
		default	= 'construction.csv',
		type	= argparse.FileType('w'),
		help	= 'path for the CSV output - construction decisions sheet')

	pars.add_argument('-e', '--estimates', 
		metavar	= "OUTPUT2", 
		default	= 'estimates.csv',
		type	= argparse.FileType('w'),
		help 	= 'path for the CSV output - estimates sheet')
	# Get the values passed on the command line
	args = pars.parse_args()

	estimates, construction = extract_data(read_excel(args.file))
	write_csv(args.estimates, estimates)
	write_csv(args.construction, construction)