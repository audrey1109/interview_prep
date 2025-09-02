from flask import Blueprint, render_template, jsonify, redirect, request, url_for
import requests
import os

from .database import db
from .models import AnonComments

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('homepage.html')

@main_blueprint.route("/submit_comment", methods = ["POST"])
def submit_comment() :

    comment = request.get_json().get("comment")

    anon_comment = AnonComments(text = comment)
    db.session.add(anon_comment)
    db.session.commit()

    return jsonify({"status": "success", "comment": comment})

    
