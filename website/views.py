from flask import Blueprint, render_template, redirect, url_for
from flask import request
import requests
import os

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('homepage.html')