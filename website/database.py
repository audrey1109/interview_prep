"""
database.py - audrey palmer

this is added to stop cyclic imports that me and my previous team couldn't seem to
work around, i would love some input if you know how to fix this! ***
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
