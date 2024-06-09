import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configuring the application
app.config.from_object('config.Config')

# Set secret key for session management
app.secret_key = os.environ.get("SECRET_KEY", "secret_flash_key")

# Configuring the SQLAlchemy database URI directly
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/login_project3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=False)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create all tables
with app.app_context():
    db.create_all()

# Define the routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    with open("data/restaurants.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        place = request.form.get("place")
        rating = request.form.get("rating")
        comments = request.form.get("comments")
        
        new_message = Message(name=name, place=place, rating=rating, comments=comments)
        db.session.add(new_message)
        db.session.commit()
        
        flash(f"Thanks {name}, we have received your review for {place}!")
        return redirect(url_for('contact'))
    
    return render_template("contact.html", page_title="Leave a Review")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['username'] = username
                flash(f"Welcome back, {username}!")
                return redirect(url_for('index'))
            else:
                flash("Invalid username or password")
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
    return render_template("login.html", page_title="Login")

@app.route('/register/', methods=['GET', 'POST'])
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
