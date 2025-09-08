'''

'''

from datetime import datetime, timezone
from flask_login import login_user, login_required, logout_user
from flask import Blueprint, flash, render_template, jsonify, redirect, request, url_for
import requests
import os

from .database import db
from .models import User, Page, Visit

pf = Blueprint("pf", __name__)


# USER FUNCTIONS ----------------------------------------------------------------

@pf.route("/sign_up", methods = ["GET", "POST"])
def sign_up() :

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

            return render_template("sign_up.html", case = "user_taken")
        
        dumme = User.query.filter_by(email = email).first()

        if dumme :
        
            return render_template("sign_up.html", case = "email_taken")

        

        new_vessel = User(username = username, email = email)
        new_vessel.set_password(password)

        db.session.add(new_vessel)
        db.session.commit()

        return render_template("sign_up.html", case = "success")

    return render_template("sign_up.html")


@pf.route("/login", methods = ["GET", "POST"])
def login() :

    if request.method == "POST" :
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username = username).first()

        if user and user.check_password(password = password) :

            login_user(user)
            return render_template("login.html", case = "success")
        
        elif user and not user.check_password(password = password) :
            
            return render_template("login.html", case = "wrong_pass")
        
        else :

            return render_template("login.html", case = "none_user")
        
    return render_template("login.html")