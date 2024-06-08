import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "private, must-revalidate"
    response.headers["Expires"] = "Wed, 21 Oct 2026 07:28:00 GMT"
    return response

db = SQL("sqlite:///users.db")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("please enter your username", 400)
        elif not password:
            return apology("please enter your password", 400)
        elif not confirmation:
            return apology("please confirm your password", 400)
        elif confirmation !=password:
            return apology("passwords don't match", 400)
        
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) == 1:
            return apology("Username already exists", 400)
        
        hashed_password = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES (?)", (username, hashed_password))
        
