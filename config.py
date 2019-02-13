#dev-config.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = ""
	SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URI'] 
	SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True
	TESTING = True

class TestingConfig(Config):
	TESTING = True