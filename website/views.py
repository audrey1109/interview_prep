from flask import Blueprint, render_template, jsonify, redirect, request, url_for
import requests
import os

from .database import db
from .models import User, Page, Visit
# from .page_functions import get_comments


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/', methods=['GET', 'POST'])
def homepage():

    return render_template('homepage.html')
