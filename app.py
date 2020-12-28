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
def index():
    '''Home page route'''
    return render_template("index.html")


@app.route("/tips")
def tips():
    """
    On the tips page, pulls through every indiviudal tip from the tips
    collection in MongoDB then sorts it in order that the tip has been added,
    newest to oldest.
    """
    category = list(mongo.db.tips.find().sort("tip_date", -1))
    return render_template("tips.html", category=category)


@app.route('/tips/<category_name>')
def filter_tips(category_name):
    """
    Acts as a filter on the tips.html page. User clicks on the filter and the
    tips with the corresponding category_name is found from the database and
    then displayed in order, again newest to oldest.
    """
    category = list(mongo.db.tips.find({
        "category_name": category_name}).sort("tip_date", -1))
    return render_template(
        "tips.html", category=category, page_title=category_name)


@app.route('/tip/<tip_id>')
def tip_page(tip_id):
    """
    Creates individual tip page. Finds the correct tip based on the
    tips's tip_id.
    """
    category = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    return render_template("tip.html", category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function on the tips.html page where the user can search any 
    word from the individual tip.
    """
    query = request.form.get("query")
    category = list(mongo.db.tips.find({"$text": {"$search": query}}))
    return render_template("tips.html", category=category)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    On the register page, initially checks if the username already exists
    in the database and flashes a message if so. Werkzeug is used to hash the
    password and post it to the database. The new user info is then formed
    into a session cookie.
    """
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
    """
    Initially checks to see if the username already exists in the
    database. If so, the hashed password is then checked to match
    user input. If not correct, a message if flashed and the user is
    redirected. If the username is not found, they are also redirected.
    """
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
    """
    First, gets the user's name from the database, and then displays
    the relavant tips.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    tips = list(mongo.db.tips.find())
    return render_template("profile.html", tips=tips)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Removes user from the session cookie and redirects them
    to the tips page.
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("tips"))


@app.route("/add_tip", methods=["GET", "POST"])
def add_tip():
    """
    On the add_tip page, adds all of the filled in fields to the database by
    using the insert_one function.
    """
    if request.method == "POST":
        tip = {
            "category_name": request.form.get("category_name"),
            "tip_name": request.form.get("tip_name"),
            "tip_short": request.form.get("tip_short"),
            "tip_long": request.form.get("tip_long"),
            "tip_img": request.form.get("tip_img"),
            "tip_date": request.form.get("tip_date"),
            "created_by": session["user"],
        }
        mongo.db.tips.insert_one(tip)
        flash("Tip Successfully Added")
        return redirect(url_for(
            "profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("tip_date", -1)
    return render_template("add_tip.html", categories=categories)


@app.route("/edit_tip/<tip_id>", methods=["GET", "POST"])
def edit_tip(tip_id):
    """
    Loads the tip that has already been added and then uses the update
    function by selecting the correct tip_id.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "tip_name": request.form.get("tip_name"),
            "tip_short": request.form.get("tip_short"),
            "tip_long": request.form.get("tip_long"),
            "tip_img": request.form.get("tip_img"),
            "tip_date": request.form.get("tip_date"),
            "created_by": session["user"],
        }
        mongo.db.tips.update({"_id": ObjectId(tip_id)}, submit)
        flash("Tip Successfully Updated")
        return redirect(url_for(
            "profile", username=session["user"]))

    tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    categories = mongo.db.categories.find().sort("tip_date", -1)
    return render_template("edit_tip.html", tip=tip, categories=categories)


@app.route("/delete_tip/<tip_id>")
def delete_tip(tip_id):
    """
    Deletes the tip by finding the matching tip using tip_id.
    """
    mongo.db.tips.remove({"_id": ObjectId(tip_id)})
    flash("Tip Successfully Deleted")
    return redirect(url_for(
            "profile", username=session["user"]))


@app.route("/manage_all")
def manage_all():
    '''Loads all tips for the admin to then read/update/delete'''
    all_tips = list(mongo.db.tips.find().sort("category_name", 1))
    return render_template("manage_all.html", all_tips=all_tips)


@app.errorhandler(403)
def forbidden(error):
    '''Handles any 403 error'''
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def not_found(error):
    '''Handles any 404 error'''
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    '''Handles any 500 error'''
    return render_template('errors/500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
