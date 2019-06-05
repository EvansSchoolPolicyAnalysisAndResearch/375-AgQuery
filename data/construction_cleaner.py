#!python3

#data/construction_cleaner.py

"""
This script modifies the indicator construction sheet of EPAR's Agricultural
Indicator Estimate Project into a format which can imported into the indicator
query tool's database. It requires said sheet to be exported as a CSV. It 
ouputs a cleaned versions of the file to construction_cleaned.csv and 
construction_countries_cleaned.csv
"""

__copyright__ = """
Copyright 2019 Evans Policy Analysis and Research Group (EPAR).
"""

__license__ = """
This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

import csv
#import argparse
INDCOLUMN = 0

instruments = ("ETH ESS Wave 1", "ETH ESS Wave 2", "ETH ESS Wave 3", "NGA GHSP Wave 1", "NGA GHSP Wave 2", "NGA GHSP Wave 3", "TZA NPS Wave 1", "TZA NPS Wave 2", "TZA NPS Wave 3", "TZA NPS Wave 4")


def read_decisions(infile):
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

	get_id = make_id_counter()
	# Get rid of the headers
	rows.pop(0)

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
		indcons.append(row_stub)
		for i,inst in enumerate(instruments):
			 cntrycons.append([get_id(), inst, row[i+15], row_stub[INDCOLUMN]])
	return (indcons, cntrycons)

def write_decisions(rows, outfile):
	"""
	Writes  a CSV stored as a list of lists from memory to disk
	
	:param rows		: a list of csv rows (lists) to be written
	:param outfile	: an open file for writing
	"""
	wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
					quoting=csv.QUOTE_NONNUMERIC)
	wrter.writerows(rows)

if __name__ == "__main__":
	import argparse

	# Setup commandline arguments
	pars = argparse.ArgumentParser( description = __doc__,
		epilog 			= __copyright__ + __license__,
		formatter_class	= argparse.ArgumentDefaultsHelpFormatter)
	
	pars.add_argument( 'file', 
		nargs	='?',
		metavar	= 'INPUT',
		type	= argparse.FileType('r'),
		default	='construction.csv', 
		help	= "path for the raw CSV file")
	
	pars.add_argument('-g', '--indicator', 
		metavar	= 'OUTPUT1', 
		default	= 'construction_cleaned.csv',
		type	= argparse.FileType('w'),
		help	= 'path for the cleaned CSV output - indicator decisions')

	pars.add_argument('-c', '--country', 
		metavar	= "OUTPUT2", 
		default	= 'construction_countries_cleaned.csv',
		type	= argparse.FileType('w'),
		help 	= 'path for the cleaned CSV output - country-level decisions')

	# Get the values passed on the command line
	args = pars.parse_args()

	# Clean the file
	indcons, cntrycons = clean_decisions(read_decisions(args.file))
	# Write the output to files
	write_decisions(indcons, args.indicator)
	write_decisions(cntrycons, args.country)