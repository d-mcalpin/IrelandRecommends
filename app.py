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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
