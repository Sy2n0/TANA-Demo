from flask import Flask, redirect, render_template, url_for, request
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    pass

@app.route("/login_done")
def login_done():
    pass

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_done")
def register_done():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="12345", debug=True)