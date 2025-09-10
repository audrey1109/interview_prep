'''
blueprint_pages.py - audrey palmer

sets up the main blueprint of my app, mostly html files which do not have a lot
of other functions to them other than hosting links

*   open to reformatting, last time when intensive function pages were included in
    the same file, it got egregiously long and confusing
'''

from flask import Blueprint, render_template, jsonify, redirect, request, url_for
from flask_login import current_user, login_required
import requests
import os

from .database import db
from .helper_functions import (defining_absent_page, increment_page_views)
from .models import User, Page, Visit


bp = Blueprint('bp', __name__)


@bp.route('/', methods=['GET', 'POST'])
def landing_page():

    # defining the page in database if not previously
    page = defining_absent_page('landing_page')
    increment_page_views(page)

    return render_template('landing_page.html')

@bp.route('/welcome_home', methods=['GET', 'POST'])
@login_required
def user_landing():

    # defining the page in database if not previously
    page = defining_absent_page('user_landing')
    increment_page_views(page)

    return render_template('user_landing.html')
