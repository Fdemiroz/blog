from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
	return "login"

@auth.route("/sign-up")
def sing_up():
	return "Sign Up"

@auth.route("/logout")
def logout():
	return "logout"