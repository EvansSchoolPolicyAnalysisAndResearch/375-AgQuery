#data/construction_cleaner.py
"""
Copyright 2019 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

import csv

def make_id_counter():
	next_id = 1
	def id_counter():
		nonlocal next_id
		id_num = next_id
		next_id += 1
		return id_num
	return id_counter

instruments = ("ETH ESS Wave 1", "ETH ESS Wave 2", "ETH ESS Wave 3", "NGA GHSP Wave 1", "NGA GHSP Wave 2", "NGA GHSP Wave 3", "TZA NPS Wave 1", "TZA NPS Wave 2", "TZA NPS Wave 3", "TZA NPS Wave 4")


# Clean the construction csv exported from the Excel File
with open('construction.csv', newline='') as infile:
	with open('construction_cleaned.csv', 'w', newline='') as outfile:
		with open('construction_countries_cleaned.csv', 'w', newline='') as cntry:
			rdr = csv.reader(infile, delimiter=',', quotechar='"', 
				quoting=csv.QUOTE_NONNUMERIC)
			wrtr = csv.writer(outfile, delimiter=',', quotechar='"', 
				quoting=csv.QUOTE_NONNUMERIC)
			cntry_wrtr = csv.writer(cntry, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
			get_id = make_id_counter()

			for r,row in enumerate(rdr):
				# Postgres does not like having headers, so this removes them
				if r == 0:
					continue
				row_stub = row[0:15]
				
				# Clean the data up a bit
				for i,elem in enumerate(row_stub) :
					if elem == "0 ":
						row_stub[i] = 0
					elif elem == "1": 
						row_stub[i] = 1
					elif type(elem) == str:
						row_stub[i] = elem.strip()
					else:
						row_stub[i] = elem
				wrtr.writerow(row_stub)
				for i,inst in enumerate(instruments):
					# Note Row Stub 2 is the varnamestem
					cntry_row = [get_id(), inst, row[i+15], row_stub[2]]
					cntry_wrtr.writerow(cntry_row)
