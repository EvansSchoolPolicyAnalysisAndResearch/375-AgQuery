#app/dlhelper.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from app.models import Estimates

def make_csv(headers, data):
	"""
	Creates a CSV given a set of headers and a list of database query results

	:param headers: A list containg the first row of the CSV
	:param data:	The list of query results from the Database
	:returns: 		A str containing a csv of the query results
	"""
	# Create a list where each entry is one row of the CSV file, starting
	# with the headers
	csvRows =[','.join(headers),]

	# Iterate through the provided data and create the rest of the CSV's rows
	for datum in data:
		currentRow = ''
		for header in headers:
			# Get this rows value for the given header
			val = getattr(datum, header)
			if type(val) is str:
				# Escape the strings
				currentRow += '"'  + val + '",'
			elif type(val) is float:
				# Don't Escape the floats
				currentRow += str(val) + ','
			else:
				# If it is empty and a place holder
				currentRow += ','
		csvRows.append(currentRow[:-1])
		
	# Combine all of the rows into a single single string and return it.
	return "\n".join(csvRows)
