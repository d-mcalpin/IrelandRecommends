import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/reviews")
def reviews():
    # On the reviews page, every indiviudal review from the reviews
    # collection in MongoDB then sorts it in order that
    # the review has been added,
    # newest to oldest.
    category = list(mongo.db.reviews.find().sort("review_date", -1))
    return render_template("reviews.html", category=category)


@app.route('/reviews/<category_name>')
def filter_reviews(category_name):
    # Acts as a filter on the tips.html page. User clicks on the filter and the
    # tips with the corresponding category_name is found from the database and
    # then displayed in order, again newest to oldest.
    category = list(mongo.db.reviews.find({
        "category_name": category_name}).sort("review_date", -1))
    return render_template(
        "reviews.html", category=category, page_title=category_name)


# holder for review page and review id


# holder for review search function


@app.route("/register", methods=["GET", "POST"])
def register():
    # On the register page, initially checks if the username already exists
    # in the database and flashes a message if so. Werkzeug is used to hash the
    # password and post it to the database. The new user info is then formed
    # into a session cookie.
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get(
                "username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Initially checks to see if the username already exists in the
    # database. If so, the hashed password is then checked to match
    # user input. If not correct, a message if flashed and the user is
    # redirected. If the username is not found, they are also redirected.
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                    session["user"] = request.form.get(
                        "username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
