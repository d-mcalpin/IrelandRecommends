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


@app.route('/review/<review_id>')
def review_page(review_id):
    # Creates individual tip page. Finds the correct tip based on the
    # tips's tip_id.
    category = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("review.html", category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function on the tips.html page where the user can search any
    word from the individual tip.
    """
    query = request.form.get("query")
    category = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", category=category)


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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # First, gets the user's name from the database, and then displays
    # the relavant reviews.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    reviews = list(mongo.db.reviews.find())
    return render_template("profile.html", reviews=reviews)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Removes user from the session cookie and redirects them
    # to the reviews page.
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("reviews"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    # On the add_review page, adds all of the filled in fields to the database by
    # using the insert_one function.
    if request.method == "POST":
        review = {
            "category_name": request.form.get("category_name"),
            "review_name": request.form.get("review_name"),
            "review_short": request.form.get("review_short"),
            "review_long": request.form.get("review_long"),
            "review_img": request.form.get("review_img"),
            "review_date": request.form.get("review_date"),
            "created_by": session["user"],
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for(
            "profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("review_date", -1)
    return render_template("add_review.html", categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # Loads the review that has already been added and then uses the update
    # function by selecting the correct review_id.
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "review_name": request.form.get("review_name"),
            "review_short": request.form.get("review_short"),
            "review_long": request.form.get("review_long"),
            "review_img": request.form.get("review_img"),
            "review_date": request.form.get("review_date"),
            "created_by": session["user"],
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for(
            "profile", username=session["user"]))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort("review_date", -1)
    return render_template(
        "edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # Deletes the review by finding the matching review using review_id.
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for(
            "profile", username=session["user"]))


@app.route("/manage_all")
def manage_all():
    # Loads all tips for the admin to then read/update/delete
    all_reviews = list(mongo.db.reviews.find().sort("category_name", 1))
    return render_template("manage_all.html", all_reviews=all_reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
