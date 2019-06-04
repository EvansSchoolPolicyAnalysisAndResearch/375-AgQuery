#!/usr/bin/python3
# data/estimates_cleaner.py

"""
This script modifies the estimates sheet of EPAR's Agricultural Indicator
Estimate Project into a format which can imported into the indicator query
tool's database. It requires said sheet to be exported as a CSV. It ouputs a 
cleaned version of the file to estimates_cleaned.csv
"""
import csv

__copyright__ = """
Copyright 2019 Evans Policy Analysis and Research Group (EPAR). 
"""
__license__ = """
This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

INDICATORCOL=6
CROPCOL=8

"""headers = ["id", "geography", "survey", "instrument", "year", "indicatorCategory", "indicatorName", "units", "cropDisaggregation", "genderDisaggregation", "farmSizeDisaggregation", "ruralortotal", "subpopulation", "currencyConversion", "indicatorLevel", "weight", "variableName", "mean", "se", "sd", "p25", "median", "p75", "minim", "maxim", "n", "nover30"]
"""
def read_estimates(infile):
	"""
	Reads a CSV File  into memory

	:param infile	: an open file for reading
	:returns		: A list of lists containing the contents of the csv file
	"""
	rows = []
	rdr = csv.reader(infile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_NONNUMERIC)
	for row in rdr:
		rows.append(row)
	return rows

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
		for i,elem in enumerate(row) :
			if elem == "0 ":
				row[i] = 0
			elif elem == "1": 
				row[i] = 1
			elif type(elem) == str:
				row[i] = elem.strip()

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
		output.append(row)
	return output
				

def write_estimates_cleaned(rows, outfile):	
	"""
	Writes  a CSV stored as a list of lists from memory to disk
	
	:param rows		: a list of csv rows (lists) to be written
	:param outfile	: an open file for writing
	"""
	wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
		quoting=csv.QUOTE_MINIMAL)
	wrtr.writerows(rows)

if __name__ == "__main__":
	import argparse

	# Parse commandline arguments
	pars = argparse.ArgumentParser(description = __doc__, 
		epilog = __copyright__ + __license__,
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	pars.add_argument('file', nargs='?', 
		default	= 'estimates.csv',
		metavar	= "INPUT",
		type	= argparse.FileType('r'),
		help 	= "path for the raw CSV file")

	pars.add_argument('-o', '--output', 
		default	= "estimates_cleaned.csv", 
		metavar	= 'OUTPUT',
		type	= argparse.FileType('w'),
		help	= 'path for the cleaned CSV output file')

	# Parse passed arguments
	args = pars.parse_args()

	write_estimates_cleaned(clean_estimates(read_estimates(args.file)), 
		args.output)
