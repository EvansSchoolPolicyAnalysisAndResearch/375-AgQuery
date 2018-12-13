#app/models.py

"""
Copyright 2018 Evans Policy Analysis and Research Group (EPAR)

This project is licensed under the 3-Clause BSD License. Please see the 
license.txt file for more information.
"""

from sqlalchemy import Column,Integer,String
from app.database import Base

class Estimates(Base):
	__tablename__ = 'Estimates'