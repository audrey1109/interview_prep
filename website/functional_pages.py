'''
functional_pages.py - audrey palmer

sets up the functional blueprint of my app, mostly html files which are associated
with function intensive work in their definition

* open to reformatting, last time when intensive function pages were included in
  the same file, it got egregiously long and confusing
'''

from datetime import datetime, timezone
from flask_login import login_user, login_required, logout_user
from flask import Blueprint, flash, render_template, jsonify, redirect, request, url_for
import requests
import os

from .database import db
from .models import User, Page, Visit

fp = Blueprint("fp", __name__)


# USER FUNCTIONS ----------------------------------------------------------------

@fp.route("/sign_up", methods = ["GET", "POST"])
def sign_up() :
    ''' returns the sign up page and defines what happens on a POST'''

    # when (on the sign up page) a user attempts to sign up
    if request.method == "POST" :

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirm-password")
        print(password)
        print(confirmation)

        if password != confirmation :
            return render_template("sign_up.html", case = "conf")
        
        dummy = User.query.filter_by(username = username).first()

        if dummy :
            # someone exists under that username already
            return render_template("sign_up.html", case = "user_taken")
        
        dumme = User.query.filter_by(email = email).first()

        if dumme :
            # someone exists under that email already
            return render_template("sign_up.html", case = "email_taken")

        
        # no other limits, creates the user
        new_vessel = User(username = username, email = email)
        new_vessel.set_password(password)

        db.session.add(new_vessel)
        db.session.commit()

        return render_template("sign_up.html", case = "success")

    return render_template("sign_up.html")


@fp.route("/login", methods = ["GET", "POST"])
def login() :
    ''' returns the login page and defines what happens on a POST'''

    # when (on the login page) a user attempts to log in
    if request.method == "POST" :
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username = username).first()

        if user and user.check_password(password = password) :
            # success
            login_user(user)
            return render_template("login.html", case = "success")
        
        elif user and not user.check_password(password = password) :
            # wrong password
            return render_template("login.html", case = "wrong_pass")
        
        else :
            # no such user
            return render_template("login.html", case = "none_user")
        
    return render_template("login.html")