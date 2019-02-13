#eparData.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the
license.txt file for more information.
"""
# Note the as application is to conform with the Gunicorn expected use of 
# application rather than app
from app import app as application
from dotenv import load_dotenv
import os

if __name__ == '__main__':
	# Load up the local settings
	local_path = os.path.dirname(os.path.abspath(__file__))
	dotenv_path = os.path.join(local_path, '.env')

	load_dotenv(dotenv_path)
    application.run()
