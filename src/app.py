from flask import request
from flask import Flask, render_template, session, redirect
from helpers import login_required
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from flask_session import Session
from flask import request, flash
from flask_mail import Mail, Message


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'CS50BW@GMAIL.COM'
app.config['MAIL_PASSWORD'] = 'eqee jbdp wdzl grfy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
db = SQL("sqlite:///events.db")
Session(app)
mail = Mail(app)



#@login required
@app.route("/login", methods = ["POST", "GET"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return "enter a username"
        
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return "invalid username and/or password"
        email = rows[0]["email"]
        if email == "ben":
            session["user_id"] = rows[0]["id"] 
            return render_template("admin.html")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/register", methods = ["POST", "GET"])
def register():
        if request.method == "POST":
            if not request.form.get("email"):
                return "must provide email"

            elif not request.form.get("password"):
                return "must provide password"

            elif not request.form.get("confirmation"):
                return "must confirm password"

            elif request.form.get("confirmation") != request.form.get("password"):
                return "passwords must match"

            elif db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email")):
                return "username already exists"

            else:
                db.execute("INSERT INTO users (email, hash) Values (?,?)", request.form.get("email"),generate_password_hash(request.form.get("password")),)
                rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))
                session["user_id"] = rows[0]["id"]
                return redirect("/")
        else:
            return render_template("register.html")

@app.route("/")
@login_required
def index():
    rows = db.execute("SELECT * from event")
    return render_template("index.html", rows=rows)

@app.route("/logout")
@login_required
def logout():
    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(port = 8000, debug=True)

@app.route("/contact", methods = ["POST", "GET"])
@login_required
def contact():
        if request.method == "POST":
            event = request.form.get("event")
            organization = request.form.get("organization")
            link = request.form.get("link")
            description = request.form.get("description")
            time = request.form.get("time")
            kind = request.form.get("kind")
            email = request.form.get("email")
            if not event:
                return "enter an event"
            elif not organization:
                return "add an organization"
            elif not time:
                return "add a time"
            else:
                msg = Message( 'Hello', sender ='CS50BW@gmail.com', recipients = ['CS50BW@gmail.com'] ) 
                msg.body = 'Event: ' + event + ' organization: ' + organization + ' link: ' + link + ' Description: ' + description + " time :" + time + " type: " + kind + " email: " + email
                mail.send(msg) 

                return redirect("/")
        else:
            return render_template("contact.html")

@app.route("/admin", methods = ["POST", "GET"])
@login_required
def admin():
    if request.method == "POST":
        email = request.form.get("email")
        event = request.form.get("event")
        organizer = request.form.get("organizer")
        link = request.form.get("link")
        description = request.form.get("description")
        time = request.form.get("time")
        kind = request.form.get("type")
        if not event:
            return "enter an event"
        elif not organizer:
            return "add an organization"
        elif not time:
            return "add a time"
        else:
            db.execute("INSERT into event(email, event, organizer, time , link, type, description) Values(?,?,?,?,?,?,?)", email, event, organizer, time, link, kind, description)
            return render_template("admin.html")
    else:
        return render_template("admin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/help")
@login_required
def help():
    return render_template("help.html")
