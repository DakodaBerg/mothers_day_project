from flask_app import app
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template("home.html")
