#app/dlhelper.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from app.models import Estimates

def make_csv(headers, data):
	csvRows =[','.join(headers),]
	for datum in data:
		currentRow = ''
		for header in headers:
			val = getattr(datum, header)
			if type(val) is str:
				currentRow += '"'  + val + '",'
			elif type(val) is float:
				currentRow += str(val) + ','
			else:
				currentRow += ','
		csvRows.append(currentRow[:-1])
		
	# Combine all of the rows into a single row.
	return "\n".join(csvRows)