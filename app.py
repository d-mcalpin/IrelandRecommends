import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/tips")
def tips():
    # """
    # On the reviews page, every indiviudal review from the reviews
    # collection in MongoDB then sorts it in order that 
    # the review has been added,
    # newest to oldest.
    # """
    category = list(mongo.db.reviews.find().sort("review_date", -1))
    return render_template("reviews.html", category=category)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
