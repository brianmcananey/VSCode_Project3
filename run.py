import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brianmcananey:password@localhost/msp3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)



# Create all tables in the database
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    with open("data/restaurants.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        content = request.form.get("content")
        new_message = Message(name=name, content=content)
        db.session.add(new_message)
        db.session.commit()
        flash(f"Thanks {name}, we have received your message!")
        return redirect(url_for('contact'))
    return render_template("contact.html", page_title="Leave a Review")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            flash(f"Welcome back, {username}!")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
    return render_template("login.html", page_title="Login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Account created for {username}!")
        return redirect(url_for('login'))
    return render_template('signup.html', page_title="Register to leave a review")


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
