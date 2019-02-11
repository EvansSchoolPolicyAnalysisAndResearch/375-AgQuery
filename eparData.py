#eparData.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the
license.txt file for more information.
"""
# Note the as application is to conform with the Gunicorn expected use of 
# application rather than app
from app import app as application

if __name__ == '__main__':
	application.run()
