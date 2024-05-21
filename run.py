import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, session


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret_flask_key")



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    data = []
    with open("data/restaurants.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(request.form.get("name")))
    return render_template("contact.html", page_title="Leave a Review")


@app.route('/login', methods =['GET', 'POST'])
def login():
    return render_template("" , page_title="Login")
 
 
@app.route('/register', methods =['GET', 'POST'])
def register():
        return render_template( '', page_title="Register to leave a review")



# change debug to false before project submit 

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)