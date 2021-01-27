#!/usr/bin/env python3

#data/ict.py

__copyright__ = """
Copyright 2021 Evans Policy Analysis and Research Group (EPAR).
"""

__license__ = """
This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

#import that shit
import os
import xlrd
import re

"""
	IND_COL: col number for the indicator name
	GD_COL: col number for the gender disaggregation info
	FS_COL: col number for the farm size disaggregation info
	CD_COL: col number for the commodity disaggregation info
	SP_COL: col number for the subpopulation of estimates info
"""

EXCEL_WORKBOOK	= 'indicator-workbook.xlsx'
IND_COL = 0
GD_COL = 3
FS_COL = 4
CD_COL = 5
SP_COL = 6

workbook = xlrd.open_workbook(EXCEL_WORKBOOK, on_demand = True)
sheets = workbook.sheet_names()
con_name = [sheet for sheet in sheets if "Indicator Construction" in sheet]
sheet = None
if len(con_name) == 1:
	sheet = workbook.sheet_by_name(con_name[0])
else:
	print("Could not find construction sheet, assuming third sheet by index")
	sheet = workbook.sheet_by_index(2)
cats = {}

#########################
# create the categories #
#########################

for x in range(sheet.nrows):
	if x == 0: continue
	ind = sheet.cell_value(x, IND_COL)
	
	# combine to
	key = re.sub(r'[^\w]', '', sheet.cell_value(x, GD_COL)).lower()
	key += re.sub(r'[^\w]', '', sheet.cell_value(x, FS_COL)).lower()
	key += re.sub(r'[^\w]', '', sheet.cell_value(x, CD_COL)).lower()
	key += "2subpops" if "(2 sub-pops):" in sheet.cell_value(x,SP_COL) else ""

	if key in cats:
		cats[key].append(ind)
	else:
		cats[key] = [ind]

#####################
# format the output #
#####################

ctr = 1
output = ""

for key in cats:
	output += "group %i\n========\n\n" % (ctr)
	ctr +=1	

	# specify the type of gender disaggregation available for this category
	output += "gender disaggregation\n:\t"
	if "genderoftheheadofhousehold" in key:
		output += "head of household"
	elif "genderoftheplotmanager" in key:
		output += "plot manager"
	elif "genderoftheindividual" in key:
		output += "individual"
	else:
		output += "none"
	output += "\n\n"

	# Add farm size disaggregation information
	output += "farm size disaggregation\n:\t%s\n\n" % \
		("yes" if "yes" in key else "no")

	# add in information about commodity disaggregation
	output += "commodity disaggregation\n:\t"
	if "allcropsmaize" in key:
		output += "all crops + bmgf list"
	elif "maize" in key:
		output += "bmgf list"
	elif "alllargeruminantscow" in key:
		output += "milk animals"
	elif "alllivestocklarge" in key:
		output += "all livestock + ls categories"
	elif "largeruminants" in key:
		output += "livestock categories"
	else:
		output += "none"
	output += "\n\n"

	# add in information about the num of subpopulations
	output += "multiple sub-populations\n:\t%s\n" % \
		("yes" if "2subpops" in key else "no")

	# add the indicators
	output += "\nindicators\n----------\n\n"
	output += "\n".join(["-\t%s" % ind for ind in cats[key]])

	output += "\n\n"


print(output)