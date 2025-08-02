
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

##helpers functions used from the course's previous assignments
from helpers import apology, login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///project.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
@login_required
def hello():
    user_id = session["user_id"]
    db1 = db.execute("SELECT essay, name,promptname, deadline, complete FROM essays WHERE username = ? ORDER BY deadline", user_id)
    return render_template("intro.html", db = db1)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
       password1 = request.form.get("password")
       password2 = request.form.get("confirmation")
       if not request.form.get("username"):
        return ("must provide username", 400)
       elif not request.form.get("password"):
        return ("must provide password", 400)

       elif password1 != password2:
        return ("Passwords do not match", 400)

       else:
        usernamecount = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(usernamecount) != 0:
            return ("Sorry!This username already exists", 400)
        else:
            newuser = db.execute("INSERT INTO users (username, password) VALUES (?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")))

    session["user_id"] = newuser
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        if not request.form.get("username"):
            return ("must provide username", 403)

# Ensure password was submitted
        elif not request.form.get("password"):
            return ("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

# Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

# Redirect user to home page
        return redirect("/")

@app.route("/input" , methods=["GET", "POST"])
def input():
    if request.method == "GET":
        return render_template("input.html")
    else:
        user_id = session["user_id"]
        essay = request.form.get("essay")
        name = request.form.get("name")
        promptname = request.form.get("promptname")
        deadline = request.form.get("deadline")
        db.execute("INSERT INTO essays (username, essay, name, promptname, deadline) VALUES(?,?,?,?,?)", user_id, essay, name, promptname, deadline)
        flash("Submit successfull")
        return render_template("input.html")


@app.route("/index" , methods=["GET", "POST"])
def index():
    user_id = session["user_id"]
    db1 = db.execute("SELECT essay, name,promptname, deadline, complete FROM essays WHERE username = ? ORDER BY deadline", user_id)
    x = False
    if request.method == "GET":
        return render_template("index.html",db=db1, x=x)
    if request.method == "POST":
        return (request.form.get("complete"))



@app.route("/delete" , methods=["GET", "POST"])
def delete():
    user_id = session["user_id"]
    db1 = db.execute("SELECT essay, name,promptname, deadline, complete FROM essays WHERE username = ? ORDER BY deadline", user_id)
    if request.method == "GET":
        return render_template("delete.html",db=db1)
    else:
        essay = request.form.get("essay")
        db.execute("DELETE FROM essays WHERE username = ? AND essay = ?", user_id, essay)
        return render_template("index.html", db = db1)


if __name__ == "__main__":
    app.run(debug=True)