from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "asdfasdf@#aksdjflkasjlaksjdf!aksjf"
DB = DBModule()

@app.route("/")
def index():
    if "uid" in session:
        user = session["uid"]
    else:
        user = "Login"
    return render_template("index.html", user = user)

@app.route("/login")
def login():
    if "uid" in session:
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/login_done", methods = ["get"])
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid, pwd):
        session["uid"] = uid
        return redirect(url_for("index"))
    else:
        flash("아이디가 없거나 비밀번호가 틀립니다.")
        return redirect(url_for("login"))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_done", methods = ["get"])
def register_done():
    email = request.args.get("email")
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    if DB.register(email = email, _id_ = uid, pwd = pwd, name = name):
        return redirect(url_for("login"))
    else:
        flash("이미 존재하는 아이디 입니다.")
        return redirect(url_for("register"))

@app.route("/logout")
def logout():
    if "uid" in session:
        session.pop("uid")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="12345", debug=True)
