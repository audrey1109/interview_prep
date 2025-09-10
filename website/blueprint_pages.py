'''
blueprint_pages.py - audrey palmer

sets up the main blueprint of my app, mostly html files which do not have a lot
of other functions to them other than hosting links

* open to reformatting, last time when intensive function pages were included in
  the same file, it got egregiously long and confusing
'''

from flask import Blueprint, render_template, jsonify, redirect, request, url_for
import requests
import os

from .database import db
from .models import User, Page, Visit
# from .page_functions import get_comments


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def homepage():
  return render_template('landing_page.html')
