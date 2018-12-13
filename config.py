#dev-config.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""
from dotenv import load_dotenv
import os

local_path = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(local_path, '.env')
sqlite_path = os.path.join(local_path, 'data', 'Estimates.db')
load_dotenv(dotenv_path)
###############################################################################
#      Modify this for the local settings and configuration needs of the      #
#                             instance in question                            #
###############################################################################
# Enable Debugging
DEBUG = True
SQLALCHEMY_DATABASE_URI='sqlite:///%s' % (sqlite_path)
SQLALCHEMY_TRACK_MODIFICATIONS=False

