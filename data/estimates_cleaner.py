#!/usr/bin/python3
# data/estimates_cleaner.py

"""
This script modifies the estimates sheet of EPAR's Agricultural Indicator
Estimate Project into a format which can imported into the indicator query
tool's database. It requires said sheet to be exported as a CSV. It ouputs a 
cleaned version of the script to estimates_cleaned.csv
"""
import csv, argparse

__copyright__ = """\
Copyright 2019 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""



INDICATORCOL=6
CROPCOL=8

"""headers = ["id", "geography", "survey", "instrument", "year", "indicatorCategory", "indicatorName", "units", "cropDisaggregation", "genderDisaggregation", "farmSizeDisaggregation", "ruralortotal", "subpopulation", "currencyConversion", "indicatorLevel", "weight", "variableName", "mean", "se", "sd", "p25", "median", "p75", "minim", "maxim", "n", "nover30"]
"""
def clean_estimates(filename):
	# Clean the estimates csv exported from the Excel File 
	with open(filename, newline='') as infile:
		with open('estimates_cleaned.csv', 'w', newline='') as outfile:
			rdr = csv.reader(infile, delimiter=',', quotechar='"', 
				quoting=csv.QUOTE_NONNUMERIC)
			wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
				quoting=csv.QUOTE_MINIMAL)
			for r,row in enumerate(rdr):
				# Postgres does not like having headers, so this removes them
				if r == 0:
					continue
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
					else:
						row[i] = elem
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

				wrtr.writerow(row)
if __name__ == "__main__":

	pars = argparse.ArgumentParser(description = __doc__, 
		epilog = __copyright__,
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	pars.add_argument( 'file', nargs='?', default='estimates.csv', 
		help = "the name of the csv file containing the indicator estimates")
	args = pars.parse_args()

	clean_estimates(args.file)
