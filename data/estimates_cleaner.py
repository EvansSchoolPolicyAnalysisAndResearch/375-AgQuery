#data/csv_cleaner.py
"""
Copyright 2019 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

import csv
INDICATORCOL=6
CROPCOL=8
headers = ["id", "geography", "survey", "instrument", "year", "indicatorCategory", "indicatorName", "units", "cropDisaggregation", "genderDisaggregation", "farmSizeDisaggregation", "ruralortotal", "subpopulation", "currencyConversion", "indicatorLevel", "weight", "variableName", "mean", "se", "sd", "p25", "median", "p75", "minim", "maxim", "n", "nover30"]

# Clean the estimates csv exported from the Excel File 
with open('estimates.csv', newline='') as infile:
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



